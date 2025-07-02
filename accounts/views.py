from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from .models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Menentukan permission secara dinamis.
        - 'create' (signup) boleh diakses siapa saja (AllowAny).
        - 'signin' boleh diakses siapa saja (AllowAny).
        - Aksi lainnya harus terautentikasi (IsAuthenticated).
        """
        if self.action == 'create' or self.action == 'signin':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # Override method 'create' untuk dijadikan 'signup'
    def create(self, request, *args, **kwargs):
        """
        Endpoint untuk pendaftaran user baru.
        URL: POST /api/users/
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Buat token langsung setelah user berhasil dibuat
        token, created = Token.objects.get_or_create(user=user)

        headers = self.get_success_headers(serializer.data)
        
        # Sertakan token dalam response
        response_data = {
            "message": "User created successfully",
            "user": serializer.data,
            "token": token.key
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'])
    def signin(self, request):
        """
        Endpoint untuk login user.
        URL: POST /api/users/signin/
        """
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user) # Opsional, untuk session-based auth jika diperlukan
            return Response({
                "message": "Login successful", 
                "token": token.key,
                "user_id": user.pk,
                "email": user.email
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def signout(self, request):
        """
        Endpoint untuk logout user.
        URL: POST /api/users/signout/
        """
        # Hapus token autentikasi user
        request.user.auth_token.delete()
        
        # Logout dari session (jika menggunakan session auth juga)
        logout(request)

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
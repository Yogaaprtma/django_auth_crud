# Proyek Tugas C: Django Full-stack Auth & CRUD

Ini adalah proyek full-stack yang dibangun menggunakan **Django** dan **Django Rest Framework (DRF)** sebagai pemenuhan Tugas C dalam proses seleksi Software Engineer di PT Informatika Media Pratama.

Aplikasi ini menyediakan REST API yang fungsional dan aman untuk otentikasi (SignUp, SignIn, SignOut) dan operasi CRUD (Create, Read, Update, Delete) untuk data pengguna.

## Fitur-fitur Utama

- **Pendaftaran Pengguna (Sign Up)**: Endpoint publik untuk membuat akun pengguna baru dengan password yang di-hash secara aman.
- **Login Pengguna (Sign In)**: Endpoint publik untuk memverifikasi kredensial pengguna dan menghasilkan token otentikasi sebagai kunci akses.
- **Logout Pengguna (Sign Out)**: Endpoint terlindungi untuk menghapus token otentikasi yang sedang aktif, secara efektif mengakhiri sesi pengguna.
- **Manajemen Pengguna (CRUD)**:
  - **Read**: Pengguna terotentikasi dapat melihat daftar pengguna lain dan detail profil masing-masing.
  - **Update**: Pengguna dapat memperbarui data profil mereka sendiri.
  - **Delete**: Pengguna dapat menghapus akun mereka.
- **Keamanan dengan Token**: Sebagian besar endpoint dilindungi dan memerlukan `Authorization Token` yang valid untuk bisa diakses.
- **Model Pengguna Kustom**: Menggunakan `CustomUser` yang mewarisi dari `AbstractUser` Django untuk menambahkan field tambahan seperti `phone_number` dan `address`.

## Teknologi yang Digunakan

- **Python**
- **Django**
- **Django Rest Framework (DRF)**
- **DRF Token Authentication**
- **SQLite** (sebagai database development)

---

## Dokumentasi API Endpoint

Berikut adalah daftar endpoint yang tersedia:

| Aksi | Method | Endpoint | Memerlukan Auth? |
| :--- | :--- | :--- | :--- |
| **Pendaftaran** | `POST` | `/api/users/` | Tidak |
| **Login** | `POST` | `/api/users/signin/` | Tidak |
| **Logout** | `POST` | `/api/users/signout/` | **Ya** |
| **Lihat Semua User** | `GET` | `/api/users/` | **Ya** |
| **Lihat Detail User** | `GET` | `/api/users/{id}/` | **Ya** |
| **Update User** | `PUT` / `PATCH` | `/api/users/{id}/` | **Ya** |
| **Hapus User** | `DELETE`| `/api/users/{id}/` | **Ya** |

---

## Instalasi dan Cara Menjalankan

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

**1. Prasyarat**
- Pastikan Anda sudah menginstal **Python 3.8+** dan **pip**.

**2. Clone & Setup**
```bash
# Clone repository ini (jika belum)
git clone https://github.com/Yogaaprtma/django_auth_crud

# Masuk ke direktori proyek Django
cd django-auth-crud
```

**3. Virtual Environment & Dependencies**
```bash
# (Rekomendasi) Buat dan aktifkan virtual environment
python -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
# venv\Scripts\activate    # Untuk Windows

Install dependencies:
pip install django==5.2.3 djangorestframework

**4. Database Setup**
```bash
# Jalankan migrasi untuk membuat tabel-tabel database
python manage.py migrate

# (Opsional) Jalankan seeder untuk membuat user 'admin' dengan password 'admin123'
python manage.py seedusers
```

**5. Jalankan Server**
```bash
# Jalankan development server
python manage.py runserver
```
Aplikasi akan berjalan di `http://127.0.0.1:8000`.

## Cara Melakukan Pengujian

Gunakan aplikasi API client seperti **Postman** atau **Insomnia** untuk berinteraksi dengan endpoint yang telah didokumentasikan di atas.

**Alur Pengujian Umum:**
1.  Gunakan endpoint **Pendaftaran** (`POST /api/users/`) untuk membuat user baru.
2.  Gunakan endpoint **Login** (`POST /api/users/signin/`) dengan kredensial yang baru dibuat untuk mendapatkan token.
3.  Salin token tersebut.
4.  Untuk mengakses endpoint yang **Memerlukan Auth**, tambahkan **HTTP Header** `Authorization` dengan value `Token <token_anda>`. Contoh: `Authorization: Token e4a5b...`
5.  Uji endpoint lain seperti melihat daftar user, update, dan terakhir **Logout**.

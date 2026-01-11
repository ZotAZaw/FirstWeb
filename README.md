# Website nghe nhạc trực tuyến được xây dựng bằng **Django**

## Giới thiệu

Chức năng chính:
- Người dùng đăng ký / đăng nhập
- Tạo album, thêm bài hát
- Nghe nhạc trực tuyến
- Tìm kiếm bài hát
- Trang cá nhân người dùng
- Quên mật khẩu (Password Reset)
- Phân quyền đăng nhập / đăng xuất


---

## Công nghệ sử dụng

- **Backend**: Python 3.10 + Django
- **Database**: SQLite (mặc định) / có thể thay bằng PostgreSQL, MySQL
- **Frontend**: Django Template + HTML + CSS
- **Authentication**: Django Auth (Login, Logout, Password Reset)
- **Static files**: CSS, Image
- **Server**: Django Development Server

---

## Yêu cầu hệ thống

- Python >= 3.9
- pip
- Git (optional)

---

## Cài đặt môi trường

### 1. Clone project

```bash
git clone https://github.com/ZotAZaw/main.git
cd main
```

### 2. Cài đặt môi trường

```bash 
pip install django
```

Trong trường hợp dùng môi trường ảo
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Chạy Server

```bash 
python manage.py runserver
```
Mở trình duyệt: http://127.0.0.1:8000/

---

## Chức năng chính:

**Authentication**
  
- Đăng ký tài khoản

- Đăng nhập

- Đăng xuất

- Quên mật khẩu (Password Reset qua email – cần cấu hình email backend)

**Music**
  
- Tạo album

- Thêm bài hát vào album

- Hiển thị danh sách bài hát

- Nghe nhạc

**Tìm kiếm**
  
- Tìm kiếm bài hát theo tên

- Thanh tìm kiếm nằm giữa thanh navigation

**Profile**
  
- Trang cá nhân người dùng

- Quản lý album của người dùng

---

## Tài khoản Admin:

Thêm tài khoản:
```bash
python manage.py createsuperuser
```

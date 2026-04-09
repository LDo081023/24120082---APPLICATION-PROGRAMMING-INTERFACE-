BÀI TẬP LAB 1: API DỊCH THUẬT ANH - VIỆT

1. THÔNG TIN SINH VIÊN
- Họ và tên: Đỗ Bá Lâm
- MSSV: 24120082

2. CÔNG NGHỆ SỬ DỤNG
- Ngôn ngữ: Python
- Framework: FastAPI
- Model AI: Helsinki-NLP/opus-mt-en-vi (Hugging Face)

3. HƯỚNG DẪN CÀI ĐẶT
Chạy lệnh sau để cài đặt các thư viện cần thiết:
pip install fastapi uvicorn transformers torch requests

5. HƯỚNG DẪN CHẠY CHƯƠNG TRÌNH
Bước 1: Khởi động Server (Terminal 1)
cd Translate
uvicorn Main:app --reload

Bước 2: Chạy file kiểm tra (Terminal 2)
python testAPI.py

Bước 3: Kiểm tra giao diện trực quan
Truy cập đường dẫn: http://127.0.0.1:8000/docs, sau đó "run it out", thay câu cần dịch vào "string" và excute

5. CÁC ENDPOINT CHÍNH
- GET / : Trang giới thiệu hệ thống
- GET /health : Kiểm tra trạng thái model
- POST /predict : Nhận văn bản tiếng Anh và trả về kết quả dịch tiếng Việt

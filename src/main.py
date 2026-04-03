import os

def send_secure_report():
    # Triệu hồi Secret từ biến môi trường hệ thống
    api_key = os.environ.get('MY_SECRET_API_KEY')
    
    if not api_key:
        print("❌ Lỗi: Không tìm thấy API Key trong hệ thống!")
        return False
    
    print(f"✅ Đang kết nối tới Server với Key: {api_key[:4]}****")
    print("🚀 Gửi báo cáo thành công!")
    return True

if __name__ == "__main__":
    send_secure_report()

import re

def validate_email(email):
    # Regex đơn giản kiểm tra email
    pattern = r'a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    # Kiểm tra số điện thoại Việt Nam (10 số, bắt đầu bằng 0)
    pattern = r'0\d{9}'
    return bool(re.match(pattern, phone))
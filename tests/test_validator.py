from src.validator import validate_email, validate_phone

def test_email_logic():
    assert validate_email("test@gmail.com") is True
    assert validate_email("invalid-email") is False

def test_phone_logic():
    assert validate_phone("0901234567") is True
    assert validate_phone("123456") is False # Thiếu số
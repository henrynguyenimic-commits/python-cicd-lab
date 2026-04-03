from src.logic import tinh_tong

def test_tinh_tong():
    assert tinh_tong(5, 5) == 10
    assert tinh_tong(-1, 1) == 0

from myapp.main import add

def test_add():
    """Тест для функции add."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

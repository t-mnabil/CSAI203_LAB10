from models.user import User


def test_user_creation():
    u = User(1, "Alice", "a@x.com")
    assert u.id == 2
    assert u.name == "Alice"
    assert u.email == "a@x.com"

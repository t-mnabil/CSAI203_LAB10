from unittest.mock import patch
from repositories.user_repository import UserRepository


@patch("core.file_singleton.FileManager.read_csv")
def test_get_all_users_csv(mock_read):
    mock_read.return_value = [
        {"id": "1", "name": "Sara", "email": "s@s.com"}
    ]

    repo = UserRepository()
    users = repo.get_all()

    assert users[0].name == "Sara"

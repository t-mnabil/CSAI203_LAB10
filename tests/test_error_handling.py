# 1. Testing "User Not Found" Scenario
from unittest.mock import MagicMock, patch

# User not found → 404


@patch("controllers.user_controller.RepositoryFactory")
def test_user_not_found_returns_404(mock_factory, client):
    mock_repo = MagicMock()
    mock_repo.get_by_id.return_value = None
    mock_factory.get_repository.return_value = mock_repo

    response = client.get("/users/999")

    assert response.status_code == 404
    assert b"User not found" in response.data

   # Repository exception → 500
# ________________________________________
# 2. Testing Repository Exception Handling
# This checks how the controller handles an unexpected DB failure.


@patch("controllers.user_controller.RepositoryFactory")
def test_repository_exception_handled(mock_factory, client):
    mock_repo = MagicMock()
    mock_repo.get_all.side_effect = Exception("Database failed")
    mock_factory.get_repository.return_value = mock_repo

    response = client.get("/users/")

    assert response.status_code == 500
    assert b"Internal Server Error" in response.data


# Create user invalid input → 400
# ________________________________________
# 3. Testing Input Validation(If implemented)
# Example: creating a user without a name.


def test_create_user_invalid_input(client):
    response = client.post("/users/create", data={
        "name": "",
        "email": "test@test.com"
    })

    assert response.status_code == 400
    assert b"Invalid name" in response.data


# ________________________________________
# 4. Testing Unexpected Route Behavior
# Ensures broken logic does not crash the application.


def test_unexpected_behavior(client):
    response = client.get("/users/something-invalid")
    assert response.status_code in (400, 404)

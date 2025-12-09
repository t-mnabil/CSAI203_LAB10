import os
import tempfile
from app import app
from core.file_singleton import FileManager


def test_integration_user_list_route(client):
    # Create a temporary CSV for the integration test
    fd, path = tempfile.mkstemp()
    os.close(fd)

    with open(path, 'w') as f:
        f.write("id,name,email\n")
        f.write("1,Amina,amina@test.com\n")

    # Force FileManager to use this file
    fm = FileManager()
    fm.file_path = path

    response = client.get('/users/')

    assert response.status_code == 200
    assert b"Amina" in response.data

    os.remove(path)

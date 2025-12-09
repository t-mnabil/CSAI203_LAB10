from core.file_singleton import FileManager


def test_singleton_file_manager():
    f1 = FileManager()
    f2 = FileManager()
    assert f1 is f2


# from core.db_singleton import DatabaseConnection

# def test_singleton_instance():
#     db1 = DatabaseConnection()
#     db2 = DatabaseConnection()
#     assert db1 is db2

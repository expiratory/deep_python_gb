import json
import pytest
from python_sem_14 import User, Project, AccessError, LevelError


# Создаем фикстуру для временного файла с данными пользователей
@pytest.fixture
def user_data_file(tmp_path):
    file_path = tmp_path / "test_users.json"
    data = [{'name': "User1", 'id': 1, 'access_level': 1}]
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return file_path


# Фикстура для создания проекта для каждого теста
@pytest.fixture
def project_instance(user_data_file):
    project = Project(user_data_file)
    return project


@pytest.mark.xfail(raises=AccessError)
def test_add_user_with_sufficient_access_level(project_instance):
    user = User("User2", 2, 2)
    project_instance.add_user(user)
    assert user in project_instance.users


@pytest.mark.xfail(raises=AccessError)
def test_add_user_with_insufficient_access_level(project_instance):
    user = User("User2", 2, 3)
    with pytest.raises(LevelError):
        project_instance.add_user(user)


def test_login_existing_user(project_instance):
    access_level = project_instance.login("User1", 1)
    assert access_level == 1


def test_login_non_existing_user(project_instance):
    with pytest.raises(AccessError):
        project_instance.login("User2", 2)


@pytest.mark.xfail(raises=AccessError)
def test_save_users_to_file(project_instance, user_data_file):
    user = User("User2", 2, 2)
    project_instance.add_user(user)
    project_instance.save_users_to_file(user_data_file)
    with open(user_data_file, 'r') as file:
        data = json.load(file)
    assert len(data) == 2


def test_save_users_to_file_empty(project_instance, user_data_file):
    project_instance.users = set()  # Устанавливаем пустое множество пользователей
    project_instance.save_users_to_file(user_data_file)
    with open(user_data_file, 'r') as file:
        data = json.load(file)
    assert len(data) == 0

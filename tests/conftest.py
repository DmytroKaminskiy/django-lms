import pytest
from django.core.management import call_command
from rest_framework.test import APIClient

from groups.models import Group


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', f'tests/fixtures/groups.json')
        call_command('loaddata', f'tests/fixtures/students.json')



@pytest.fixture()
def group():
    # print('BEFORE')
    group_object = Group.objects.create(name='Name', course='Course')
    yield group_object
    group_object.delete()
    # print('deleted')
    # print('AFTER')


@pytest.fixture(scope='function')
def client_api():
    client = APIClient()
    return client

# @pytest.fixture(scope='session', autouse=True)
# def example():
#     print('FOO')
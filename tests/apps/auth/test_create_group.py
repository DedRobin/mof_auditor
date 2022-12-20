import pytest

from django.test.client import Client
from faker import Faker
from apps.users.factories import UserFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.user.set_password("password")
        self.user.save()
        self.fake = Faker()

    def test_create_group(self):
        self.client.force_login(self.user)
        data = {"name": "some name", "description": "some description"}
        response = self.client.post("/groups/create/", data=data)
        assert response.status_code == 302
        assert response.url == "/"

import pytest

from django.test.client import Client
from faker import Faker

from tests.factories import *


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.user.set_password("password")
        self.user.save()
        self.fake = Faker()

    def test_index(self):
        response = self.client.get("/")
        assert response.status_code == 302
        assert response.url == "/auth/login?next=/"

    def test_register_login_logout(self):
        data = {
            "username": self.fake.user_name(),
            "password": self.fake.md5(),
        }
        response = self.client.get("/auth/register/")
        assert response.status_code == 200
        response = self.client.post("/auth/register/", data=data)
        assert response.status_code == 302
        assert response.url == "/auth/login/"

        response = self.client.post("/auth/login/", data=data)
        assert response.status_code == 302
        assert response.url == "/"

        response = self.client.get("/auth/logout/")
        assert response.status_code == 302
        assert response.url == "/auth/login/"

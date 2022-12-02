import pytest
import random
from django.test.client import Client
from faker import Faker

from tests.factories import UserFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.user.set_password("password")
        self.user.save()
        self.fake = Faker()

    def test_register(self):
        response = self.client.get("/api/auth/register/")
        assert response.status_code == 200

        register_data = {
            "username": self.fake.user_name(),
            "password": self.fake.md5(),
            "gender": random.choice(["male", "female"]),
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        response = self.client.post("/api/auth/register/", data=register_data)
        assert response.status_code == 201

    def test_login(self):
        response = self.client.get("/api/auth/login/")
        assert response.status_code == 200

        data_register = {
            "username": self.fake.user_name(),
            "password": self.fake.md5(),
            "email": self.fake.email(),
            "gender": random.choice(["male", "female"]),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        response = self.client.post("/api/auth/register/", data=data_register)
        assert response.status_code == 201

        data_login = {
            "username": data_register["username"],
            "password": data_register["password"],
        }

        response = self.client.post("/api/auth/login/", data=data_login)
        assert response.status_code == 200

    def test_login_2(self):
        response = self.client.get("/api/auth/login/")
        assert response.status_code == 200

        data_login = {"username": self.user.username, "password": "password"}

        response = self.client.post("/api/auth/login/", data=data_login)
        assert response.status_code == 200

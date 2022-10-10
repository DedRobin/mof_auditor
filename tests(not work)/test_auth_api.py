import pytest
from faker import Faker
from django.test.client import Client

from tests.factories import UserFactory


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.user.set_password("password")
        self.user.save()
        self.fake = Faker()

    # @pytest.mark.skip
    def test_register(self):
        response = self.client.get("/api/register/")
        assert response.status_code == 200

        data_register = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.md5(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        response = self.client.post("/api/register/", data=data_register)
        assert response.status_code == 201

    # @pytest.mark.skip
    def test_login(self):
        response = self.client.get("/api/login/")
        assert response.status_code == 200

        data_register = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.md5(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        response = self.client.post("/api/register/", data=data_register)
        assert response.status_code == 201

        data_login = {
            "username": data_register["username"],
            "password": data_register["password"]
        }

        response = self.client.post("/api/login/", data=data_login)
        assert response.status_code == 200

    # @pytest.mark.skip
    def test_login_2(self):
        response = self.client.get("/api/login/")
        assert response.status_code == 200

        data_login = {
            "username": self.user.username,
            "password": "password"
        }

        response = self.client.post("/api/login/", data=data_login)
        assert response.status_code == 200

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
        assert response.url == "/login?next=/"

    def test_register_login_logout(self):
        data = {
            "username": self.fake.word(),
            "password": self.fake.md5(),
        }
        response = self.client.get("/register/")
        assert response.status_code == 200
        response = self.client.post("/register/", data=data)
        assert response.status_code == 302
        assert response.url == "/login/"

        response = self.client.get("/login/")
        assert response.status_code == 200
        response = self.client.post("/login/", data=data)
        assert response.status_code == 302
        assert response.url == "/"

        response = self.client.get("/logout/")
        assert response.status_code == 302
        assert response.url == "/login/"

    # def test_login(self):
    #     response = self.client.get("/")
    #     assert response.status_code == 302
    #     assert response.url == f"/login?next=/"

    # def test_get_posts(self):
    #     ProductFactory.create_batch(10)

    # response = self.client.get("/shop/products/")
    # assert response.status_code == 200
    # assert response.content.count("product_card") == 10

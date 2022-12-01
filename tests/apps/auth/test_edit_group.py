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

        self.client.force_login(self.user)

    def test_get_page_for_create_group(self):
        response = self.client.get("/groups/create/")
        assert response.status_code == 200

    def test_create_group(self):
        # self.client.force_login(self.user)

        data = {"name": "some name", "description": "some description"}
        response = self.client.post("/groups/create/", data=data)
        assert response.status_code == 302
        assert response.url == "/"

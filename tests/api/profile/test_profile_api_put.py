import pytest
import random
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.profiles.factories import ProfileFactory
from apps.profiles.models import GENDER_CHOICE


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.random_gender = random.choice(
            [codename for codename, name in GENDER_CHOICE if codename is not None]
        )
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()
        self.content_type = "application/json"
        self.client.force_login(self.user)

    def test_profile_put(self):
        ProfileFactory(user=self.user)

        data = {
            "gender": self.random_gender,
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        url = "/api/profile/"

        response = self.client.put(url, data=data, content_type=self.content_type)
        assert response.status_code == 200
        assert response.data["gender"] == data["gender"]
        assert response.data["email"] == data["email"]
        assert response.data["first_name"] == data["first_name"]
        assert response.data["last_name"] == data["last_name"]

    def test_profile_patch(self):
        ProfileFactory(user=self.user)

        data = {
            "gender": self.random_gender,
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        url = "/api/profile/"

        for key, value in data.items():
            response = self.client.patch(url, data={key: value}, content_type=self.content_type)
            assert response.status_code == 200
            assert response.data[key] == data[key]

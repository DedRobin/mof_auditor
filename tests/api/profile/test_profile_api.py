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

    def test_profile_get(self):
        self.client.force_login(self.user)
        ProfileFactory(user=self.user)

        response = self.client.get("/api/profile/")
        assert response.status_code == 200
        assert response.data["email"] == self.user.profile.email
        assert response.data["gender"] == self.user.profile.gender
        assert response.data["first_name"] == self.user.profile.first_name
        assert response.data["last_name"] == self.user.profile.last_name

    def test_profile_put(self):
        self.client.force_login(self.user)
        ProfileFactory(user=self.user)

        data = {
            "gender": self.random_gender,
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        content_type = "application/json"

        response = self.client.put(
            "/api/profile/", data=data, content_type=content_type
        )
        assert response.status_code == 200
        assert response.data["gender"] == data["gender"]
        assert response.data["email"] == data["email"]
        assert response.data["first_name"] == data["first_name"]
        assert response.data["last_name"] == data["last_name"]

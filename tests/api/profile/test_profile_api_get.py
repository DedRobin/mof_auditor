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

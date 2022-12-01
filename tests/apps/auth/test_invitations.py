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

    def test_get_invitation_list(self):
        self.client.force_login(self.user)

        response = self.client.get("/groups/invitations/")
        assert response.status_code == 200

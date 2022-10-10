import pytest
from faker import Faker
from django.test.client import Client

from tests.factories import UserFactory


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    def test_index(self):
        self.client.force_login(self.user)

        response = self.client.get("/api/posts/")
        assert response.status_code == 200

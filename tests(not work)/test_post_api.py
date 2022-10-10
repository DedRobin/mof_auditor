import pytest
from faker import Faker
from django.test.client import Client

from tests.factories import UserFactory, PostFactory


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    def test_create_posts(self):
        self.client.force_login(self.user)

        PostFactory.create_batch(5, author=self.user)
        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert response.data["count"] == 5

    def test_create_one_post(self):
        self.client.force_login(self.user)

        data = {"title": "title", "slug": "slug", "text": "text"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert response.data["count"] == 1
        assert "image" in response.data["results"][0]

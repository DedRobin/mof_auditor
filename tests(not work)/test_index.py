import pytest

from django.test.client import Client
from faker import Faker

from tests.factories import *


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    def test_index(self):
        response = self.client.get("/")
        assert response.status_code == 302
        assert response.url == "/shop/products/"

    def test_get_posts(self):
        ProductFactory.create_batch(10)

        response = self.client.get("/shop/products/")
        assert response.status_code == 200
        # assert response.content.count("product_card") == 10


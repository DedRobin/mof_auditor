import pytest
from collections import OrderedDict
from django.test.client import Client
from tests.factories import UserFactory, ProductFactory, PurchaseFactory
from shop.models import Purchase


@pytest.mark.django_db
class TestPurchasesViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()

    def test_get_product_list(self):
        ProductFactory.create_batch(21)
        response = self.client.get("/api/products/")
        assert response.status_code == 200
        assert response.data["count"] == 21

    def test_search_product(self):
        ProductFactory(title="test_product_title_1", cost=10, color="blue")
        ProductFactory(title="test_product_title_2", cost=20, color="green")
        ProductFactory(title="test_product_title_3", cost=30, color="red")

        response = self.client.get(f"/api/products/?search=test_product_title_3")
        assert response.data["results"][0]["title"] == "test_product_title_3"

        response = self.client.get(f"/api/products/?search=10")
        assert response.data["results"][0]["title"] == "test_product_title_1"

        response = self.client.get(f"/api/products/?search=green")
        assert response.data["results"][0]["title"] == "test_product_title_2"

    def test_sorting_product(self):
        ProductFactory(title="apple", cost=100)
        ProductFactory(title="potato", cost=200)
        ProductFactory(title="milk", cost=30)

        response = self.client.get(f"/api/products/?ordering=title")  # title - ascending
        assert response.data["results"][0]["title"] == "apple"

        response = self.client.get(f"/api/products/?ordering=-title")  # title - descending
        assert response.data["results"][0]["title"] == "potato"

        response = self.client.get(f"/api/products/?ordering=cost")  # cost - ascending
        assert response.data["results"][0]["title"] == "milk"

        response = self.client.get(f"/api/products/?ordering=-cost")  # cost - descending
        assert response.data["results"][0]["title"] == "potato"

    def test_filter_product(self):
        ProductFactory(title="meat", cost=10)
        ProductFactory(title="banana", cost=20)
        ProductFactory(title="bread", cost=30)
        ProductFactory(title="milk", cost=40)
        ProductFactory(title="orange", cost=50)

        response = self.client.get("/api/products/?min_cost=40")
        assert response.status_code == 200
        assert response.data["count"] == 2

        response = self.client.get("/api/products/?max_cost=35")
        assert response.status_code == 200
        assert response.data["count"] == 3

        response = self.client.get("/api/products/?title=bread")
        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["title"] == "bread"

        response = self.client.get("/api/products/?min_cost=30&max_cost=50")
        assert response.status_code == 200
        assert response.data["count"] == 3

        response = self.client.get("/api/products/?min_cost=10&max_cost=30&title=meat")
        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["title"] == "meat"

    def test_complex_for_product(self):
        ProductFactory(title="meat1", cost=321, color="blue")
        ProductFactory(title="meat2", cost=945, color="green")
        ProductFactory(title="banana1", cost=432, color="red")
        ProductFactory(title="banana2", cost=834, color="red")
        ProductFactory(title="bread1", cost=12, color="blue")
        ProductFactory(title="bread2", cost=354, color="blue")
        ProductFactory(title="milk1", cost=978, color="green")
        ProductFactory(title="milk2", cost=76, color="blue")
        ProductFactory(title="orange1", cost=267, color="blue")
        ProductFactory(title="orange2", cost=1, color="green")

        response = self.client.get("/api/products/?search=7")
        assert response.data["count"] == 3

        response = self.client.get("/api/products/?search=meat&min_cost=400")
        assert response.data["count"] == 1

        response = self.client.get("/api/products/?search=milk&max_cost=75")
        assert response.data["count"] == 0

        response = self.client.get("/api/products/?search=green&min_cost=977")
        assert response.data["count"] == 1

        response = self.client.get("/api/products/?search=blue&min_cost=1&max_cost=300")
        assert response.data["count"] == 3
        all_titles = sorted([dict(x).get("title") for x in response.data["results"]])
        assert all_titles == ["bread1", "milk2", "orange1"]


    def test_purchases_list(self):
        purchase_1 = PurchaseFactory()
        self.client.force_login(purchase_1.user)
        response = self.client.get("/api/purchases/")

        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["product"]["title"] == purchase_1.product.title

        purchase_2 = PurchaseFactory(user=self.user)
        self.client.force_login(self.user)
        response = self.client.get("/api/purchases/")

        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["product"]["title"] == purchase_2.product.title

        assert Purchase.objects.count() == 2

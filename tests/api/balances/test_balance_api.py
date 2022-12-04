import pytest
from django.test.client import Client
from faker import Faker

from apps.balances.factories import UserFactory, BalanceCurrencyFactory, BalanceFactory
from apps.transactions.factories import TransactionFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()
        self.currency = BalanceCurrencyFactory()
        BalanceFactory.create_batch(size=5, owner=self.user, currency=self.currency)

    # @pytest.mark.skip
    def test_balances_get(self):
        self.client.force_login(self.user)

        response = self.client.get("/api/balances/")
        assert response.status_code == 200
        assert response.data["count"] == 5

    # @pytest.mark.skip
    def test_balances_post(self):
        self.client.force_login(self.user)
        data = {
            "name": "string",
            "type": "cash",
            "currency": self.currency,
            "private": True,
        }
        response = self.client.post("/api/balances/", data=data)
        assert response.status_code == 201
        assert response.data["count"] == 6

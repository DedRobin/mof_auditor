import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.balances.factories import CurrencyFactory, BalanceFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.other_user = UserFactory()
        self.fake = Faker()
        self.currency = CurrencyFactory()

        self.balance = BalanceFactory(owner=self.user, currency=self.currency)

        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_balances_delete(self):
        """Delete a specific balance"""

        response = self.client.get("/api/balances/")
        assert response.status_code == 200
        assert response.data["count"] == 1

        response = self.client.delete(f"/api/balances/{self.balance.id}/")
        assert response.status_code == 200

        response = self.client.get("/api/balances/")
        assert response.status_code == 200
        assert response.data["count"] == 0

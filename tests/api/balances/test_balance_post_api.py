import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.balances.factories import (
    CurrencyFactory,
    BalanceFactory,
    BALANCE_TYPE_CHOICE,
)
from apps.groups.factories import GroupFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.other_user = UserFactory()
        self.fake = Faker()
        self.currency = CurrencyFactory()

        self.data = {
            "name": "test_post",
            "currency": self.currency.id,
            "type": "cash",
            "private": False,
        }
        BalanceFactory.create_batch(size=5, owner=self.user, currency=self.currency)

        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_balances_post_with_different_currency_types(self):
        """Creating balances with different types"""

        balance_types = [codename for codename, name in BALANCE_TYPE_CHOICE]

        for balance_type in balance_types:
            self.data["type"] = balance_type

            response = self.client.post("/api/balances/", data=self.data)
            assert response.status_code == 201

        response = self.client.get("/api/balances/")
        assert response.status_code == 200
        assert response.data["count"] == 8

    def test_balances_post_with_unknown_currency_type(self):
        """Adding unknown currency type"""

        self.data["type"] = "unknown_type"
        response = self.client.post("/api/balances/", data=self.data)
        assert response.status_code == 400

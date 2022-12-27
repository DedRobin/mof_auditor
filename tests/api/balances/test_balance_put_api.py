import pytest
import copy
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.balances.factories import (
    CurrencyFactory,
    BalanceFactory,
    BALANCE_TYPE_CHOICE,
)


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

        # Initial data
        self.content_type = "application/json"
        self.data = {
            "name": self.balance.name,
            "type": self.balance.type,
            "currency": self.balance.currency.id,
            "private": self.balance.private,
        }

    # @pytest.mark.skip
    def test_balances_get(self):
        """Getting a specific balance"""

        response = self.client.get(f"/api/balances/{self.balance.id}/")
        assert response.status_code == 200
        assert response.data["id"] == self.balance.id
        assert response.data["pub_id"] == self.balance.pub_id
        assert response.data["name"] == self.balance.name
        assert response.data["owner"] == self.balance.owner.username
        assert response.data["type"] == self.balance.type
        assert response.data["currency"] == self.balance.currency.id

    # @pytest.mark.skip
    def test_balances_put_name(self):
        """Update name for a specific balance"""

        data = copy.deepcopy(self.data)

        # New name
        data["name"] = "test_name"

        response = self.client.put(
            f"/api/balances/{self.balance.id}/",
            data=data,
            content_type=self.content_type,
        )
        assert response.status_code == 200
        response = self.client.get(f"/api/balances/{self.balance.id}/")
        assert response.status_code == 200
        assert response.data["name"] == data["name"]

    # @pytest.mark.skip
    def test_balances_put_type(self):
        """Update type for a specific balance"""

        data = copy.deepcopy(self.data)
        balance_types = [codename for codename, name in BALANCE_TYPE_CHOICE]

        # New allowed types
        for balance_type in balance_types:
            data["type"] = balance_type

            response = self.client.put(
                f"/api/balances/{self.balance.id}/",
                data=data,
                content_type=self.content_type,
            )
            assert response.status_code == 200
            response = self.client.get(f"/api/balances/{self.balance.id}/")
            assert response.status_code == 200
            assert response.data["type"] == data["type"]

    # @pytest.mark.skip
    def test_balances_put_unknown_type(self):
        """Update a specific balance using unknown type"""

        data = copy.deepcopy(self.data)

        # Unknown type
        data["type"] = "bitcoin"

        response = self.client.put(
            f"/api/balances/{self.balance.id}/",
            data=data,
            content_type=self.content_type,
        )
        assert response.status_code == 400

    # @pytest.mark.skip
    def test_balances_put_currency(self):
        """Update currency for a specific balance"""

        data = copy.deepcopy(self.data)

        # New currency
        new_currency = CurrencyFactory(name="Russian Ruble", codename="RUB")
        data["currency"] = new_currency.id

        response = self.client.put(
            f"/api/balances/{self.balance.id}/",
            data=data,
            content_type=self.content_type,
        )
        assert response.status_code == 200
        response = self.client.get(f"/api/balances/{self.balance.id}/")
        assert response.status_code == 200
        assert response.data["currency"] == data["currency"]

    # @pytest.mark.skip
    def test_balances_put_private(self):
        """Update private for a specific balance"""

        data = copy.deepcopy(self.data)

        # New private (inverting bool)
        data["private"] = not data["private"]

        response = self.client.put(
            f"/api/balances/{self.balance.id}/",
            data=data,
            content_type=self.content_type,
        )
        assert response.status_code == 200
        response = self.client.get(f"/api/balances/{self.balance.id}/")
        assert response.status_code == 200
        assert response.data["private"] == data["private"]

import pytest
from django.test.client import Client
from faker import Faker
from decimal import Decimal

from apps.users.factories import UserFactory
from apps.balances.factories import BalanceCurrencyFactory, BalanceFactory, BALANCE_TYPE_CHOICE
from apps.groups.factories import GroupFactory
from apps.transactions.factories import TransactionFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.other_user = UserFactory()
        self.fake = Faker()
        self.currency = BalanceCurrencyFactory()
        self.balance = BalanceFactory(owner=self.user, currency=self.currency)
        self.transactions = TransactionFactory.create_batch(size=3, balance=self.balance)
        self.total = sum(transaction.amount for transaction in self.transactions)
        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_balances_put(self):
        """Update data for some balance"""

        response = self.client.get(f"/api/balances/{self.balance.id}/")
        assert response.status_code == 200
        assert response.data["id"] == self.balance.id
        assert response.data["pub_id"] == self.balance.pub_id
        assert response.data["name"] == self.balance.name
        assert response.data["owner"] == self.balance.owner.username
        assert response.data["type"] == self.balance.type
        assert response.data["type"] == self.balance.type
        assert response.data["currency"] == self.balance.currency.id
        assert Decimal(response.data["total"]) == self.total
        assert len(response.data["groups"]) == len(self.balance.groups.all())

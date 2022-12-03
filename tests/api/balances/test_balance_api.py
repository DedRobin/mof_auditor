import pytest
from django.test.client import Client
from faker import Faker

from apps.balances.factories import UserFactory, BalanceCurrencyFactory, BalanceFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    # @pytest.mark.skip
    def test_balances_get(self):
        self.client.force_login(self.user)
        BalanceFactory.create_batch(size=5, owner=self.user)
        response = self.client.get("/api/balances/")
        assert response.status_code == 200
        assert response.data["count"] == 5

    @pytest.mark.skip
    def test_balances_post(self):
        pass

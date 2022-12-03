import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.balances.factories import BalanceCurrencyFactory, BalanceFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    # @pytest.mark.skip
    def test_group_get(self):
        self.client.force_login(self.user)

        response = self.client.get("/api/groups/")
        assert response.status_code == 200

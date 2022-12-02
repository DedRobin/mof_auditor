import pytest
from django.test.client import Client
from faker import Faker

from tests.factories import UserFactory, BalanceCurrencyFactory, BalanceFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

    @pytest.mark.skip
    def test_balances_get(self):
        self.client.force_login(self.user)
        BalanceCurrencyFactory()
        BalanceFactory.build_batch(5)
        response = self.client.get("/balances/")
        assert response.status_code == 200

    @pytest.mark.skip
    def test_balances_post(self):
        pass

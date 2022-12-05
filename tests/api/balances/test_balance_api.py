import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.balances.factories import BalanceCurrencyFactory, BalanceFactory, BALANCE_TYPE_CHOICE
from apps.groups.factories import GroupFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.other_user = UserFactory()
        self.fake = Faker()
        self.currency = BalanceCurrencyFactory()
        self.groups = GroupFactory.create_batch(size=3, group_info__owner=self.user)
        self.invited_group = GroupFactory(group_info__owner=self.other_user)
        # self.invited_group.invited_users.add(self.user)
        self.invited_group.invited_users.set([self.user])
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

        # Creating balances with different types
        balance_types = [codename for codename, name in BALANCE_TYPE_CHOICE]
        data = {
            "name": "test_post",
            "currency": self.currency.id,
            "private": False,
            "groups": [group.id for group in self.groups]
        }

        for balance_type in balance_types:
            data["type"] = balance_type

            response = self.client.post("/api/balances/", data=data)
            assert response.status_code == 201

        # Getting all user groups (own and invited)
        response = self.client.get("/api/balances/")
        assert response.status_code == 200
        assert response.data["count"] == 8

        # Adding a balance to invited group
        data["groups"] = [self.invited_group.id]
        response = self.client.post("/api/balances/", data=data)
        assert response.status_code == 201
        data["groups"] = [group.id for group in self.groups]

        # Adding a balance to uninvited group
        other_group = GroupFactory()
        data["groups"] = [other_group.id]
        response = self.client.post("/api/balances/", data=data)
        assert response.status_code == 400
        data["groups"] = [group.id for group in self.groups]

        # Adding unknown currency type
        data["type"] = "unknown_type"
        response = self.client.post("/api/balances/", data=data)
        assert response.status_code == 400
        data["type"] = balance_types[0]

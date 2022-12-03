import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.permissions.factories import PermissionFactory, PermissionTypeFactory
from apps.permissions.models import Permission


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

        self.permission_type_read = PermissionTypeFactory(name="read")
        self.permission_type_create = PermissionTypeFactory(name="create")
        self.permission_type_update = PermissionTypeFactory(name="update")
        self.permission_type_delete = PermissionTypeFactory(name="delete")
        self.permission_types = {
            "read": self.permission_type_read,
            "create": self.permission_type_create,
            "update": self.permission_type_update,
            "delete": self.permission_type_delete
        }

    # @pytest.mark.skip
    def test_balances_post(self):
        self.client.force_login(self.user)
        PermissionFactory.create(user=self.user, types=(self.permission_type_read, self.permission_type_update))

        response = self.client.get("/api/permissions/")
        print()

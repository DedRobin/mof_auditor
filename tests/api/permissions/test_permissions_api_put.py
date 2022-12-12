import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.permissions.factories import PermissionFactory, PermissionTypeFactory
from apps.groups.factories import GroupFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.invited_user = UserFactory()
        self.fake = Faker()
        self.group = GroupFactory(group_info__owner=self.user)

        # Default permission types
        self.permission_types = {
            name: PermissionTypeFactory(name=name) for name in
            ["read", "create", "update", "delete"]
        }
        self.read = self.permission_types["read"]
        self.create = self.permission_types["create"]
        self.update = self.permission_types["update"]
        self.delete = self.permission_types["delete"]

        self.group.invited_users.add(self.invited_user)
        self.client.force_login(self.user)

    @pytest.mark.skip
    def test_permission_put(self):
        """Update a permission"""

        permission = PermissionFactory(user=self.invited_user, group=self.group)
        url = "/api/groups/{0}/invited_users/{1}/permissions/{2}/"
        url = url.format(self.group.id, self.invited_user.id, permission.id)

        data = {
            "invited_users": [self.read, self.update]
        }

        response = self.client.put(url, data=data, content_type="application/json")
        assert response.status_code == 200

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
        self.fake = Faker()
        self.user_group = GroupFactory(group_info__owner=self.user)
        self.other_group = GroupFactory()
        self.permission_types = {
            name: PermissionTypeFactory(name=name) for name in
            ["read", "create", "update", "delete"]
        }
        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_permission_get(self):
        """Getting all user permissions"""
        user_permission = PermissionFactory(user=self.user, group=self.user_group)
        user_permission.types.add(self.permission_types["read"])
        user_permission.types.add(self.permission_types["create"])
        other_permission = PermissionFactory(user=self.user, group=self.other_group)
        other_permission.types.add(self.permission_types["update"])
        other_permission.types.add(self.permission_types["delete"])

        response = self.client.get("/api/permissions/")
        assert response.status_code == 200
        assert response.data["count"] == 2
        assert response.data["results"][0]["types"] == [self.permission_types["read"].id,
                                                        self.permission_types["create"].id]

    # @pytest.mark.skip
    def test_permission_get_one_note(self):
        """Getting all user permissions"""

        permission = PermissionFactory(user=self.user, group=self.user_group)

        response = self.client.get(f"/api/permissions/{permission.id}/")
        assert response.status_code == 200
        assert response.data["id"] == permission.id

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
        self.read = self.permission_types["read"]
        self.create = self.permission_types["create"]
        self.update = self.permission_types["update"]
        self.delete = self.permission_types["delete"]
        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_permission_get(self):
        """Getting all user permissions"""

        p_for_user_group = PermissionFactory(user=self.user, group=self.user_group)
        p_for_user_group.types.add(self.read)
        p_for_user_group.types.add(self.create)

        p_for_other_group = PermissionFactory(user=self.user, group=self.other_group)
        p_for_other_group.types.add(self.update)
        p_for_other_group.types.add(self.delete)

        response = self.client.get("/api/permissions/")
        assert response.status_code == 200
        assert response.data["count"] == 2
        assert response.data["results"][0]["types"] == [self.read.id, self.create.id]
        assert response.data["results"][1]["types"] == [self.update.id, self.delete.id]

    # @pytest.mark.skip
    def test_permission_get_one_note(self):
        """Getting all user permissions"""

        permission = PermissionFactory(user=self.user, group=self.user_group)
        permission.types.set([self.read, self.create, self.update, self.delete])

        response = self.client.get(f"/api/permissions/{permission.id}/")
        assert response.status_code == 200
        assert response.data["id"] == permission.id
        assert response.data["user"] == self.user.username
        assert response.data["group"] == self.user_group.__str__()
        assert response.data["types"] == [self.read.id, self.create.id, self.update.id, self.delete.id]

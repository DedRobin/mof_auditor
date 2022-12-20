import pytest
from django.test.client import Client
from faker import Faker

from apps.permissions.factories import PermissionTypeFactory
from apps.users.factories import UserFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()
        self.client.force_login(self.user)

        # Default permission types
        self.permission_types = {
            name: PermissionTypeFactory(name=name)
            for name in ["read", "create", "update", "delete"]
        }
        self.read = self.permission_types["read"]
        self.create = self.permission_types["create"]
        self.update = self.permission_types["update"]
        self.delete = self.permission_types["delete"]

    # @pytest.mark.skip
    def test_group_post(self):
        """Create new group"""

        data = {
            "group_info.name": "test_name",
            "group_info.description": "test_description",
        }

        response = self.client.post("/api/groups/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/groups/")
        assert response.data["count"] == 1

    # @pytest.mark.skip
    def test_group_post_without_description(self):
        """Trying to create new group without description"""

        data = {
            "group_info.name": "test_name",
        }

        response = self.client.post("/api/groups/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/groups/")
        assert response.data["count"] == 1

    # @pytest.mark.skip
    def test_group_post_without_name(self):
        """Trying to create new group without name"""

        data = {
            "group_info.description": "test_description",
        }

        response = self.client.post("/api/groups/", data=data)
        assert response.status_code == 400

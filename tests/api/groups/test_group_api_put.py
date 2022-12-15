import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.groups.factories import GroupFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()
        self.group = GroupFactory(group_info__owner=self.user)
        self.content_type = "application/json"
        self.data = {
            "group_info.name": self.group.group_info.name,
            "group_info.description": self.group.group_info.description,
        }

        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_group_put(self):
        """Change all notes"""

        response = self.client.get(f"/api/groups/{self.group.id}/")

        # Change all notes
        response.data["group_info"]["name"] = "test_name"
        response.data["group_info"]["description"] = "test_description"

        response = self.client.put(f"/api/groups/{self.group.id}/", data=response.data, content_type=self.content_type)
        assert response.status_code == 200

        response = self.client.get(f"/api/groups/{self.group.id}/")

        # Check data
        assert response.data["group_info"]["name"] == "test_name"
        assert response.data["group_info"]["description"] == "test_description"

    # @pytest.mark.skip
    def test_group_put_name(self):
        """Change a group name"""
        # Change name
        response = self.client.get(f"/api/groups/{self.group.id}/")
        response.data["group_info"]["name"] = "test_name"

        response = self.client.put(f"/api/groups/{self.group.id}/", data=response.data, content_type=self.content_type)
        assert response.status_code == 200

        # Check data
        response = self.client.get(f"/api/groups/{self.group.id}/")
        assert response.data["group_info"]["name"] == "test_name"

    # @pytest.mark.skip
    def test_group_put_description(self):
        """Change a group description"""

        response = self.client.get(f"/api/groups/{self.group.id}/")

        # Change a description
        response.data["group_info"]["description"] = "test_description"

        response = self.client.put(f"/api/groups/{self.group.id}/", data=response.data, content_type=self.content_type)
        assert response.status_code == 200

        response = self.client.get(f"/api/groups/{self.group.id}/")

        # Check data
        assert response.data["group_info"]["description"] == "test_description"

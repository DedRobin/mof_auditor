import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.groups.factories import GroupInformationFactory, GroupFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()
        self.client.force_login(self.user)
        self.group = GroupFactory(group_info__owner=self.user)
        self.content_type = "application/json"

        self.data = {
            "group_info.name": self.group.group_info.name,
            "group_info.description": self.group.group_info.description,
            "invited_users": [],
        }

    # @pytest.mark.skip
    def test_group_put(self):
        """Change all notes"""

        invited_users = UserFactory.create_batch(size=3)
        invited_users = [user.id for user in invited_users]

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Change all notes
        data["group_info"]["name"] = "test_name"
        data["group_info"]["description"] = "test_description"
        data["invited_users"] = invited_users

        response = self.client.put(f"/api/groups/{self.group.id}/", data=data, content_type=self.content_type)
        assert response.status_code == 200

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Check data
        assert data["group_info"]["name"] == "test_name"
        assert data["group_info"]["description"] == "test_description"
        assert data["invited_users"] == invited_users

    # @pytest.mark.skip
    def test_group_put_name(self):
        """Change a group name"""

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Change all notes
        data["group_info"]["name"] = "test_name"

        response = self.client.put(f"/api/groups/{self.group.id}/", data=data, content_type=self.content_type)
        assert response.status_code == 200

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Check data
        assert data["group_info"]["name"] == "test_name"

    # @pytest.mark.skip
    def test_group_put_description(self):
        """Change a group description"""

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Change a description
        data["group_info"]["description"] = "test_description"

        response = self.client.put(f"/api/groups/{self.group.id}/", data=data, content_type=self.content_type)
        assert response.status_code == 200

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Check data
        assert data["group_info"]["description"] == "test_description"

    # @pytest.mark.skip
    def test_group_put_invited_users(self):
        """Change invited users for group"""

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        invited_users = UserFactory.create_batch(size=3)
        invited_users = [user.id for user in invited_users]

        # Change invited users
        data["invited_users"] = invited_users

        response = self.client.put(f"/api/groups/{self.group.id}/", data=data, content_type=self.content_type)
        assert response.status_code == 200

        response = self.client.get(f"/api/groups/{self.group.id}/")
        data = response.data

        # Check data
        assert data["invited_users"] == invited_users

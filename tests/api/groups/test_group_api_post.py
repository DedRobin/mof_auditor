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

    # @pytest.mark.skip
    def test_group_post(self):
        """Create new group"""

        invited_users = UserFactory.create_batch(size=3)
        invited_users = [user.id for user in invited_users]

        data = {
            "group_info.name": "test_name",
            "group_info.description": "test_description",
            "invited_users": invited_users,
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

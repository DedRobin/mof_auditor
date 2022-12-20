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
        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_group_delete(self):
        """Delete a specific group"""

        group = GroupFactory(group_info__owner=self.user)

        response = self.client.get("/api/groups/")
        assert response.status_code == 200
        assert response.data["count"] == 1

        response = self.client.delete(f"/api/groups/{group.id}/")
        assert response.status_code == 200

        response = self.client.get("/api/groups/")
        assert response.status_code == 200
        assert response.data["count"] == 0

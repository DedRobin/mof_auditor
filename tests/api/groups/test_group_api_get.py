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

    # @pytest.mark.skip
    def test_group_get_all_notes(self):
        response = self.client.get("/api/groups/")
        assert response.status_code == 200
        assert response.data["count"] == 1

        GroupFactory(group_info__owner=self.user)

        response = self.client.get("/api/groups/")
        assert response.status_code == 200
        assert response.data["count"] == 2

    # @pytest.mark.skip
    def test_group_get_specific_note(self):

        response = self.client.get(f"/api/groups/{self.group.id}/")
        assert response.status_code == 200

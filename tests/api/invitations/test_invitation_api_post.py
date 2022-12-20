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

        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_invitation_post(self):
        data = {
            "from_who": self.user,
            "to_who": UserFactory(),
            "to_a_group": self.group.id,
        }

        response = self.client.post("/api/invitations/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/invitations/")
        assert response.status_code == 200
        assert response.data["count"] == 1

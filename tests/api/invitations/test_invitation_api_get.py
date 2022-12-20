import pytest
from django.test.client import Client
from faker import Faker

from apps.users.factories import UserFactory
from apps.invitations.factories import InvitationFactory


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = Faker()

        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_invitation_get_all_notes(self):
        InvitationFactory.create_batch(size=10, from_who=self.user)

        response = self.client.get("/api/invitations/")
        assert response.status_code == 200
        assert response.data["count"] == 10

    # @pytest.mark.skip
    def test_invitation_get_one_notes(self):
        invitation = InvitationFactory(from_who=self.user)

        response = self.client.get(f"/api/invitations/{invitation.id}/")
        assert response.status_code == 200
        assert response.data["id"] == invitation.id
        assert response.data["to_who"] == invitation.to_who.username
        assert response.data["from_who"] == invitation.from_who.username

    #
    #     GroupFactory(group_info__owner=self.user)
    #
    #     response = self.client.get("/api/groups/")
    #     assert response.status_code == 200
    #     assert response.data["count"] == 2
    #
    # # @pytest.mark.skip
    # def test_group_get_specific_note(self):
    #
    #     response = self.client.get(f"/api/groups/{self.group.id}/")
    #     assert response.status_code == 200

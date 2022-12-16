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
    def test_invitation_delete(self):
        invitation = InvitationFactory(from_who=self.user)

        response = self.client.get(f"/api/invitations/{invitation.id}/")
        assert response.status_code == 200

        response = self.client.delete(f"/api/invitations/{invitation.id}/")
        assert response.status_code == 200
        assert response.data is None

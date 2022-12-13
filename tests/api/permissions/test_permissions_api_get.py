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
        self.invited_user = UserFactory()
        self.fake = Faker()
        self.group = GroupFactory(group_info__owner=self.user)
        self.group.invited_users.add(self.invited_user)

        # Default permission types
        self.permission_types = {
            name: PermissionTypeFactory(name=name) for name in
            ["read", "create", "update", "delete"]
        }
        self.read = self.permission_types["read"]
        self.create = self.permission_types["create"]
        self.update = self.permission_types["update"]
        self.delete = self.permission_types["delete"]

        # Setting permission types for user
        self.p_for_user = PermissionFactory(user=self.user, group=self.group)
        self.p_for_user.types.set([self.read, self.create, self.update, self.delete])

        # Setting permission types for invited user
        self.p_for_invited_user = PermissionFactory(user=self.invited_user, group=self.group)
        self.p_for_invited_user.types.set([self.read])

        self.client.force_login(self.user)

    # @pytest.mark.skip
    def test_permission_get_through_group(self):
        """
        Getting all user permissions
        through url='api/groups/<id>/permissions/'
        """

        url = "/api/groups/{0}/permissions/"
        url = url.format(self.group.id)

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == 2
        assert response.data["results"][0]["types"] == [self.read.id, self.create.id, self.update.id, self.delete.id]
        assert response.data["results"][1]["types"] == [self.read.id]

    # @pytest.mark.skip
    def test_permission_get_one_note_through_group(self):
        """
        Getting a specific permission
        through url='api/groups/<id>/invited_users/<id>/permissions/<id>/'
        """

        url = "/api/groups/{0}/permissions/{1}/"
        url = url.format(self.group.id, self.p_for_invited_user.id)

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == self.p_for_invited_user.id
        assert response.data["types"] == [self.read.id]
        # @pytest.mark.skip

    def test_permission_get_through_invited_users(self):
        """
        Getting all user permissions
        through url='api/groups/<id>/invited_users/<id>/permissions/'
        """

        url = "/api/groups/{0}/invited_users/{1}/permissions/"
        url = url.format(self.group.id, self.user.id)

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["results"][0]["types"] == [self.read.id, self.create.id, self.update.id, self.delete.id]

        url = "/api/groups/{0}/invited_users/{1}/permissions/"
        url = url.format(self.group.id, self.invited_user.id)
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["results"][0]["types"] == [self.read.id]

    # @pytest.mark.skip
    def test_permission_get_one_note_through_invited_users(self):
        """
        Getting a specific permission
        through url='api/groups/<id>/invited_users/<id>/permissions/<id>/'
        """

        url = "/api/groups/{0}/invited_users/{1}/permissions/{2}/"
        url = url.format(self.group.id, self.invited_user.id, self.p_for_invited_user.id)

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == self.p_for_invited_user.id
        assert response.data["types"] == [self.read.id]

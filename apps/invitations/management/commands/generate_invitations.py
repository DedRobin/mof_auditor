from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.groups.models import Group
from apps.invitations.models import Invitation
from apps.invitations.factories import InvitationFactory


class Command(BaseCommand):
    help = "Generate invitations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all invitation records",
        )

    def handle(self, *args, **options):
        """Generates a unique invitation from each user"""
        if options["clear"]:
            Invitation.objects.all().delete()

        users = User.objects.all()
        size = 0
        other_users = 0
        groups = 0
        try:
            size = int(
                input(
                    "How much would you like to create invitations for each group each user?\n"
                )
            )
            if size <= 0:
                print("Size must be greater than 0.")
                return
        except ValueError:
            print("The value is incorrect.")
        else:
            for from_who in users:
                other_users = User.objects.exclude(pk=from_who.id).order_by("?")[:size]
                groups = Group.objects.filter(group_info__owner=from_who).order_by("?")[
                    :size
                ]
                for to_a_group in groups:
                    for to_who in other_users:
                        InvitationFactory(
                            from_who=from_who, to_who=to_who, to_a_group=to_a_group
                        )

        print(
            f"{size * len(other_users) * len(groups)} invitations have been created for each group each user."
        )

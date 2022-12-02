import factory.fuzzy
from factory.django import DjangoModelFactory
from apps.users.models import User
from apps.groups.models import Group, GroupInformation
from apps.profiles.models import Profile, GENDER_CHOICE
from apps.permissions.models import Permission


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.Faker("md5")


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    email = factory.Faker("email")
    gender = factory.fuzzy.FuzzyChoice(dict(GENDER_CHOICE).keys())
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    name = factory.Faker("word")
    codename = factory.Faker("word")
    users = factory.SubFactory(UserFactory)


class GroupInformationFactory(DjangoModelFactory):
    class Meta:
        model = GroupInformation

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker("word")
    description = factory.Faker("sentence")


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    group_info = factory.SubFactory(GroupInformationFactory)
    pub_id = factory.Faker("md5")
    invited_users = factory.SubFactory(UserFactory)
    permissions = factory.SubFactory(PermissionFactory)

#
#
# class ProductFactory(DjangoModelFactory):
#     class Meta:
#         model = Product
#
#     title = factory.Faker('company')
#     cost = factory.Faker("pyint", min_value=50, max_value=150)
#     color = factory.fuzzy.FuzzyChoice(dict(COLOR_CHOICES).keys())
#
#
# class PurchaseFactory(DjangoModelFactory):
#     class Meta:
#         model = Purchase
#
#     user = factory.SubFactory(UserFactory)
#     product = factory.SubFactory(ProductFactory)
#     count = factory.Faker("pyint", min_value=1, max_value=5)

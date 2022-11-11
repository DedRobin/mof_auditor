import factory.fuzzy
from factory.django import DjangoModelFactory
from apps.users.models import User
from apps.groups.models import Group, GroupInformation


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("word")
    password = factory.Faker("md5")


class GroupInformationFactory(DjangoModelFactory):
    class Meta:
        model = GroupInformation

    owner = UserFactory()
    slug = factory.Faker("word")
    text = factory.Faker("sentence")


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    title = factory.Faker("word")
    slug = factory.Faker("word")
    text = factory.Faker("sentence")


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

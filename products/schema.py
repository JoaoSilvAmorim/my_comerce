import graphene
from graphene_django import DjangoObjectType
from products.models import *
from project.execute_query import execute_query

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name")

class Query(graphene.ObjectType):
    all_products = graphene.Field(ProductType)
    products_user = graphene.List(ProductType, user=graphene.String(required=True))

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_products_user(root, info, user):
        return Product.objects.filter(user=user)

schema = graphene.Schema(query=Query)
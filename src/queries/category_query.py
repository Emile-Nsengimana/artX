import graphene

from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.models.category_model import Category as CategoryModal


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModal
        interface = (graphene.relay.Node, )


class CategoryQuery(graphene.ObjectType):
    categories = graphene.Field(Category, description='Returns all categories')

    def resolve_categories(self, info):
        _categories = CategoryModal.query.all()

        if not _categories:
            raise GraphQLError('no category found')
        return CategoryModal.query.all()

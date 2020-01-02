import graphene

from src.api.queries.user_query import UserQuery
from src.api.queries.art_query import ArtQuery
from src.api.queries.category_query import CategoryQuery
from src.api.queries.payment_query import PaymentQuery
from src.api.mutations.user_mutation import CreateUser


class Query(UserQuery, ArtQuery, CategoryQuery,
            PaymentQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

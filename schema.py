import graphene

from src.queries.user_query import UserQuery
from src.queries.art_query import ArtQuery
from src.queries.category_query import CategoryQuery
from src.queries.payment_query import PaymentQuery
from src.mutations.user_mutation import CreateUser


class Query(UserQuery, ArtQuery, CategoryQuery,
            PaymentQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

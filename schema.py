import graphene

from src.api.queries.user_query import UserQuery
from src.api.queries.art_query import ArtQuery
from src.api.queries.payment_query import PaymentQuery
from src.api.mutations.user_mutation import CreateUser, Login


class Query(UserQuery, ArtQuery,
            PaymentQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
    Login = Login.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

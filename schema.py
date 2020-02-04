import graphene

from src.api.queries.user_query import UserQuery
from src.api.queries.art_query import ArtQuery
from src.api.queries.payment_query import PaymentQuery
from src.api.mutations.user_mutation import CreateUser, Login
from src.api.mutations.art_mutation import RegisterArt


class Query(UserQuery, ArtQuery,
            PaymentQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    CreateUser = CreateUser.Field()
    Login = Login.Field()
    registerArt = RegisterArt.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

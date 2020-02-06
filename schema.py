import graphene

from src.api.queries.user_query import UserQuery
from src.api.queries.art_query import ArtQuery
from src.api.queries.order_query import OrderQuery
from src.api.queries.payment_query import PaymentQuery
from src.api.mutations.user_mutation import CreateUser
from src.api.mutations.art_mutation import RegisterArt


class Query(UserQuery, ArtQuery, OrderQuery,
            PaymentQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    CreateUser = CreateUser.Field()
    registerArt = RegisterArt.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from src.models.art_order_model import Order as OrderModal


class ArtOrder(SQLAlchemyObjectType):
    class Meta:
        model = OrderModal
        interfaces = (graphene.relay.Node,)


class OrderQuery(graphene.ObjectType):
    user_orders = graphene.List(ArtOrder, userId=graphene.String(required=True),
                                description='''Returns a list of orders''')

    def resolve_user_orders(self, info, userId):
        orders = OrderModal.query.filter_by(orderedBy=userId).all()

        if not orders:
            raise GraphQLError('no order made')
        return orders

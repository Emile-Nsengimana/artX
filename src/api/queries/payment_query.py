import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from src.models.payment_model import Payment as PaymentModel


class Payment(SQLAlchemyObjectType):
    class Meta:
        model = PaymentModel
        interface = (graphene.relay.Node, )


class PaymentQuery(graphene.ObjectType):
    payments = graphene.Field(Payment, description='Returns all payments')

    def resolve_payments(self, info):
        _payments = PaymentModel.query.all()

        if not _payments:
            raise GraphQLError('No Payment found')
        return PaymentModel.query.all()

import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from src.models.user_model import User as UserModal


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModal
        interfaces = (graphene.relay.Node,)


class UserQuery(graphene.ObjectType):
    users = graphene.List(User, description='Returns a list of all users')
    user = graphene.Field(User,
                          user_id=graphene.Int(required=True),
                          description='''Returns a specif user details by
                                          user_id(National ID)''')

    def resolve_users(self, info):
        _users = UserModal.query.all()

        if not _users:
            raise GraphQLError('no user found')
        return _users

    def resolve_user(self, info, user_id):
        _user = UserModal.query.filter_by(user_id=user_id).first()

        if not _user:
            GraphQLError('user not found')
        return _user

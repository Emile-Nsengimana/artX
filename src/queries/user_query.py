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
    user_by_username = graphene.Field(User,
                                      username=graphene.String(required=True),
                                      description='''Returns a specif user details by
                                          username''')

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

    def resolve_user_by_username(self, info, username):
        user = UserModal.query.filter_by(username=username).first()

        if not user:
            raise GraphQLError(f'{username} not found')
        return user

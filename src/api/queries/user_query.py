import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from werkzeug.security import check_password_hash

from src.models.user_model import User as UserModal
from src.helpers.auth import Authentication


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModal
        interfaces = (graphene.relay.Node,)


class UserQuery(graphene.ObjectType):

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    users = graphene.List(User, description='Returns a list of all users')
    authentication = graphene.Field(User,
                                    email=graphene.String(required=True),
                                    password=graphene.String(required=True),
                                    description="User created by this mutation.")
    token = graphene.String()
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
            raise GraphQLError('user not found')
        return _user

    def resolve_user_by_username(self, info, username):
        user = UserModal.query.filter_by(username=username).first()

        if not user:
            raise GraphQLError(f'{username} not found')
        return user

    def resolve_authentication(self, info, **kwargs):
        _user = UserModal.query.filter_by(email=kwargs['email']).first()

        if not _user:
            raise GraphQLError('email not found')

        password = check_password_hash(_user.password, kwargs['password'])
        if not password:
            raise GraphQLError('incorrect password')

        token = Authentication.generate_token({
            'user_id': _user.user_id,
            'username': _user.username,
            'first_name': _user.first_name,
            'last_name': _user.last_name,
            'email': _user.email,
            'role': _user.role
        })

        return _user(user=_user, token=token)

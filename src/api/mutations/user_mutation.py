import graphene

from graphql import GraphQLError
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.user_model import User as UserModal
from src.api.queries.user_query import User
from src.utils.validation.user_validation import Validate
from src.helpers.auth import Authentication


class CreateUser(graphene.Mutation):
    user = graphene.Field(User, description="User created by this mutation.")
    token = graphene.String()

    class Arguments:
        user_id = graphene.ID(description='National ID')
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        email = graphene.String()
        dob = graphene.Date(description='User date of birth. \
                                        \neg: 1900-01-01')
        role = graphene.String(description='''User role \
                              \neg: System admin, Customer or System user ''')
        phone_no = graphene.String(description='Telephone Number')
        country = graphene.String(description='Country of origin')
        status = graphene.String(description='State or country province')
        city = graphene.String()
        street_no = graphene.String(description='Street Number')
        post_code = graphene.String()
        password = graphene.String()

    def mutate(self, info, **kwargs):
        Validate.user_info(**kwargs)

        # password encryption
        kwargs['password'] = generate_password_hash(kwargs['password'])
        user = UserModal.save_user(**kwargs)

        token = Authentication.generate_token({
            'user_id': kwargs['user_id'],
            'username': kwargs['username'],
            'first_name': kwargs['first_name'],
            'last_name': kwargs['last_name'],
            'email': kwargs['email'],
            'role': kwargs['role']
        })

        if type(user) == str:
            raise GraphQLError(user)

        return CreateUser(user=user, token=token)


class Login(graphene.Mutation):
    user = graphene.Field(User)
    token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
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

        return Login(user=_user, token=token)

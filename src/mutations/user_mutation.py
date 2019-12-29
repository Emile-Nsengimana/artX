import graphene

from graphql import GraphQLError

from src.models.user_model import User as UserModal
from src.queries.user_query import User


class CreateUser(graphene.Mutation):
    user = graphene.Field(User, description="User created by this mutation.")

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
        is_admin = graphene.Boolean()

    def mutate(self, info, **kwargs):
        user = UserModal.save_user(**kwargs)
        if type(user) == str:
            raise GraphQLError(user)
        return CreateUser(user=user)

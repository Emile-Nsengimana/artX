import graphene

from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from src.models.art_model import Art as ArtModal
from src.api.queries.art_query import Art
from src.utils.validation.art_validation import Validate


class RegisterArt(graphene.Mutation):
    art = graphene.Field(Art, description="Art created by this mutation.")

    class Arguments:
        no = graphene.ID()
        label = graphene.String(description='''\
                              \neg: unity, agaseke ...  ''')
        image = graphene.String()
        details = graphene.String()
        price = graphene.Float()
        owner = graphene.String()
        category = graphene.String(description='''\
                              \neg: 'painting', 'drawing', 'photography', 'digital graphics' ''')
        status = graphene.String(description='''\
                              \neg: available, sold ''')

    def mutate(self, info, **kwargs):
        Validate.art_info(**kwargs)
        art = ArtModal.save_art(**kwargs)

        if type(art) == str:
            raise GraphQLError(art)
        return RegisterArt(art=art)

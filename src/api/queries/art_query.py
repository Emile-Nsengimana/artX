import graphene

from sqlalchemy.sql.expression import func
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from src.models.art_model import Art as ArtModal


class Art(SQLAlchemyObjectType):
    class Meta:
        model = ArtModal
        interfaces = (graphene.relay.Node,)


class ArtQuery(graphene.ObjectType):
    art = graphene.Field(Art, no=graphene.String(required=True),
                         description='''Returns a specific art
                                     by no(art number)''')
    arts = graphene.List(Art, description='Returns a list of all arts')

    def resolve_art(self, info, no):
        _art = ArtModal.query.filter_by(no=no).first()

        if not _art:
            raise GraphQLError('art not found')
        return _art

    def resolve_arts(self, info):
        _arts = ArtModal.query.all()

        if not _arts:
            raise GraphQLError('no art found')
        return _arts

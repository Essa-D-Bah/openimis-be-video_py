import graphene
from core.schema import OrderedDjangoFilterConnectionField, OfficerGQLType
from gql_queries import VideoGQLType



class Query(graphene.ObjectType):
    videos = OrderedDjangoFilterConnectionField(VideoGQLType,orderBy=graphene.List(of_type=graphene.String)) 
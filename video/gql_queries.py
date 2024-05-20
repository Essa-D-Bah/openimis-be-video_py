import graphene
from models import Video
from graphene_django import DjangoObjectType
from core import ExtendedConnection


class VideoGQLType(DjangoObjectType):
    """
    Main element for a Video. It can contain items and/or services.
    The filters are possible on BatchRun, Insuree, HealthFacility, Admin and ICD in addition to the Claim fields
    themselves.
    """

    class Meta:
        model = Video
        interfaces = (graphene.relay.Node,)
        exclude_fields = ('row_id')
        filter_fields = {
            "video_name": ["exact"]
        }
        connection_class = ExtendedConnection
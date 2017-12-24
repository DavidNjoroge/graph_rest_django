import graphene
from graphene_django.types import DjangoObjectType
from .models import Invetory

class InvetoryType(DjangoObjectType):
    class Meta:
        model = Invetory

class Query(object):
    all_invetories = graphene.List(InvetoryType)

    def resolve_all_invetories(self,info, **kwargs):
        return Invetory.objects.all()

    
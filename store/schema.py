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
#1
class CreateInvetory(graphene.Mutation):
    id = graphene.Int()
    category = graphene.String()
    price = graphene.Float()
    stocked = graphene.Boolean()
    name = graphene.String()
#2
    class Arguments:

        category = graphene.String()
        price = graphene.Float()
        stocked = graphene.Boolean()
        name = graphene.String()
#3
    def mutate(self,category):
        print("<><><><.,..,><?>??>?>?><><>")
        # invetory = Invetory(category=category,price=price,stocked=stocked,name=name)
        # invetory.save()

        # return CreateInvetory(

        #     id = invetory.id,
        #     category = invetory.category,
        #     price = invetory.price,
        #     stocked = invetory.stocked,
        #     name = invetory.name
        # )
#4
class Mutation(graphene.ObjectType):
    
    create_invetory = CreateInvetory.Field()
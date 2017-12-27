import graphene
import store.schema

class Query(store.schema.Query,graphene.ObjectType):
    pass

# class Mutation(store_schema.Mutation,graphene.ObjectType):
#     pass

class Mutation(store.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
import graphene
import store.schema as store_schema

class Query(store_schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
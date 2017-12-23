from django.shortcuts import render
from .models import Invetory
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import InvetorySerializer


# Create your views here.
class StoreInvetory(APIView):
    def get(self,request,format=None):
        '''
        simple api end for getting all store items from the invetory model
        '''
        all_invetory = Invetory.objects.all()
        serializers = InvetorySerializer(all_invetory,many=True)
        return Response(serializers.data)
from rest_framework import serializers
from .models import Invetory

class InvetorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Invetory
        # fields=('id','latitude','longitude','shopname')
        fields = '__all__'

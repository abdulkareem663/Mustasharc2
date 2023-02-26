from ..models import *
from rest_framework.serializers import ModelSerializer

class phoneorderSerializer(ModelSerializer):
    class Meta:
        model = phoneorder
        fields = '__all__'


class orderworkSerializer(ModelSerializer):
    class Meta:
        model = orderwork
        fields = '__all__'
from rest_framework.viewsets import ModelViewSet
from ..models import phoneorder, orderwork
from .serializers import *


class phoneorder_view(ModelViewSet):
    queryset = phoneorder.objects.all()
    serializer_class = phoneorderSerializer


class orderwork_view(ModelViewSet):
    queryset = orderwork.objects.all()
    serializer_class = orderworkSerializer

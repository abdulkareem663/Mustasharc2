from rest_framework.viewsets import ModelViewSet
from ..models import Degree, Subject, Spiecification, Service, Project, TaskProject
from rest_framework.permissions import AllowAny
from .serializers import *


class degree_view(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializers
    permission_classes = [AllowAny]


class subject_view(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers
    permission_classes = [AllowAny]


class spiecification_view(ModelViewSet):
    queryset = Spiecification.objects.all()
    serializer_class = SpiecificationSerializers
    permission_classes = [AllowAny]


class service_view(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [AllowAny]


class project_view(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    permission_classes = [AllowAny]


class task_project_view(ModelViewSet):
    queryset = TaskProject.objects.all()
    serializer_class = TaskProjectSerializers
    permission_classes = [AllowAny]

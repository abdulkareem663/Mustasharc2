from rest_framework.serializers import ModelSerializer
from ..models import Degree,Subject,Spiecification,Service,Project,TaskProject

class DegreeSerializers(ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"


class SubjectSerializers(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SpiecificationSerializers(ModelSerializer):
    class Meta:
        model = Spiecification
        fields = "__all__"

class ServiceSerializers(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ProjectSerializers(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TaskProjectSerializers(ModelSerializer):
    class Meta:
        model = TaskProject
        fields = "__all__"
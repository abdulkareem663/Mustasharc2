from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('degree/', degree_view)
router.register('subject/', subject_view)
router.register('specification/', spiecification_view)
router.register('service/', service_view)
router.register('project/', project_view)
router.register('task-project/', task_project_view)

urlpatterns = [

    path('', include(router.urls))

]

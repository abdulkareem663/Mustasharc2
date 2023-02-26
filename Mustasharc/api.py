from django.urls import include,path

urlpatterns = [
    path('center/', include('Center.api.urls')),
    path('orders/', include('orders.api.urls')),
]
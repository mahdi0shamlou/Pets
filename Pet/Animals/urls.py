from django.urls import path
from .views import ListAnimals

urlpatterns = [
    path('api/list/', ListAnimals.as_view(), name='Animals-list')
]
from django.urls import path
from .views import VaccineList

urlpatterns = [
    path('api/vaccine/', VaccineList.as_view(), name='token_obtain_pair'),

]
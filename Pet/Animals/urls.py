from django.urls import path
from .views import ListAnimals, UsersAnimlas, AddAnimals, DeleteAnimals

urlpatterns = [
    path('api/list/', ListAnimals.as_view(), name='Animals-list'),
    path('api/list/user/', UsersAnimlas.as_view(), name='Users_animals'),
    path('api/add/', AddAnimals.as_view(), name='add_user_animals'),
    path('api/delete/', DeleteAnimals.as_view(), name='delete_user_animals'),
]
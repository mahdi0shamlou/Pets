from django.urls import path
from .views import index, Login


urlpatterns = [
    path('', index, name='Index_users'),
    path('Login/', Login, name='Login'),

]

from django.urls import path
from .views import RegisterView, Profile, Update_profile
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    # path('api/users/', UsersList.as_view(), name="users_list"),
    path('api/profile/', Profile.as_view(), name="User_profile"),
    path('api/profile/update/', Update_profile.as_view(), name="User_profile_update")
]

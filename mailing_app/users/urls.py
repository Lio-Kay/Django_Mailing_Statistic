from django.urls import path

from users.apps import UsersConfig
from users.views import UserLoginView, UserLogoutView, RegisterView, verify_email, UserProfileView, UserGeneratePassword

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_form/', UserProfileView.as_view(), name='profile'),
    path('generate_password/', UserGeneratePassword.as_view(), name='generate_password'),
    path('verify_email/<str:key>', verify_email, name='verify_email'),
]
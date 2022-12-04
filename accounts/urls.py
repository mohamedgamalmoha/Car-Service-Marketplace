from django.urls import path
from .views import (LogInView, LogOutView, RegistrationView, CustomerProfileView, UpdateCustomerProfileView,
                    UserChangePasswordView)


app_name = "accounts"

urlpatterns = [
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('register/', RegistrationView.as_view(), name="registration"),
    path('profile/', CustomerProfileView.as_view(), name="profile"),
    path('profile-update/', UpdateCustomerProfileView.as_view(), name="profile_update"),
    path('change-password/', UserChangePasswordView.as_view(), name="change_password"),
]

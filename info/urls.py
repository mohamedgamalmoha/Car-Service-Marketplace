from django.urls import path

from .views import ContactUsView


app_name = "info"

urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]

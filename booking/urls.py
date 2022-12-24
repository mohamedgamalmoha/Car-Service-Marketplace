from django.urls import path
from .views import CreateBookingView, UpdateBookingView


app_name = 'booking'

urlpatterns = [
    path('create/', CreateBookingView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBookingView.as_view(), name='update'),
]

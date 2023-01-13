from django.urls import path
from .views import CreateBookingWithDiscountView, CreateBookingWithoutDiscountView, UpdateBookingView


app_name = 'booking'

urlpatterns = [
    path('create-with-discount/', CreateBookingWithDiscountView.as_view(), name='create_with_discount'),
    path('create-without-discount/', CreateBookingWithoutDiscountView.as_view(), name='create_without_discount'),
    path('update/<int:pk>/', UpdateBookingView.as_view(), name='update'),
]

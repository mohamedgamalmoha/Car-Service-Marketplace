from django.urls import path

from .views import CreateCarView, UpdateCarView, DeleteCarView


app_name = "car"

urlpatterns = [
    path('create/', CreateCarView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateCarView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCarView.as_view(), name='delete'),
]

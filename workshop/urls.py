from django.urls import path

from .views import WorkShopList, WorkShopDetail


app_name = "workshop"
urlpatterns = [
    path('search/', WorkShopList.as_view(), name='workshop_list'),
    path('detail/<int:pk>', WorkShopDetail.as_view(), name='workshop_detail'),
]

from django.urls import path

from .views import (WorkShopListView, WorkShopDetailView,
                    CreateRateView,  UpdateRateView, DeleteRateView,
                    CreateCommentView, UpdateCommentView, DeleteCommentView,
                    CreateReportIssueView, UpdateReportIssueView, DeleteReportIssueView)


app_name = "workshop"

urlpatterns = [
    path('search/', WorkShopListView.as_view(), name='workshop_list'),
    path('detail/<int:pk>/', WorkShopDetailView.as_view(), name='workshop_detail'),

    path('rate-create/', CreateRateView.as_view(), name='create_rate'),
    path('rate-update/<int:pk>/', UpdateRateView.as_view(), name='update_rate'),
    path('rate-delete/<int:pk>/', DeleteRateView.as_view(), name='delete_rate'),

    path('comment-create/', CreateCommentView.as_view(), name='create_comment'),
    path('comment-update/<int:pk>/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment-delete/<int:pk>/', DeleteCommentView.as_view(), name='delete_comment'),

    path('report-create/', CreateReportIssueView.as_view(), name='create_report'),
    path('report-update/<int:pk>/', UpdateReportIssueView.as_view(), name='update_report'),
    path('report-delete/<int:pk>/', DeleteReportIssueView.as_view(), name='delete_report'),
]

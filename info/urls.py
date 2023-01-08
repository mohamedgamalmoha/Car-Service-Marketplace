from django.urls import path

from .views import (ContactUsView, FAQsListView, AboutUsListView, TermsOfServiceListView, WorksListView,
                    CookiePolicyListView, PrivacyPolicyListView)


app_name = "info"

urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('FAQs/', FAQsListView.as_view(), name='FAQs'),
    path('about-us/', AboutUsListView.as_view(), name='about_us'),
    path('terms-of-service/', TermsOfServiceListView.as_view(), name='terms_of_service'),
    path('how-it-works/', WorksListView.as_view(), name='works'),
    path('cookie-policy/', CookiePolicyListView.as_view(), name='cookie_policy'),
    path('privacy-policy/', PrivacyPolicyListView.as_view(), name='privacy_policy'),
]

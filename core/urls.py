"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

from .views import HomePage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', HomePage.as_view(), name='home'),
    path('i18n/', include('django.conf.urls.i18n')),
    *i18n_patterns(
        path('info/', include('info.urls', namespace="info")),
        path('auth/', include('accounts.urls', namespace="accounts")),
        path('auth/social/', include('allauth.urls')),
        path('workshop/', include('workshop.urls', namespace="workshop")),
        path('car/', include('car.urls', namespace="car")),
        path('booking/', include('booking.urls', namespace="booking")),
        path('blog/', include('blog.urls', namespace="blog")),
        path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    ),
]

# Handlers for error pages
handler400 = 'core.views.bad_request_view'
handler403 = 'core.views.permission_denied_view'
handler404 = 'core.views.page_not_found_view'
handler500 = 'core.views.error_view'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

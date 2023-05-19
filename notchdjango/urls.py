"""
URL configuration for notchdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Notch",
        default_version='1.1.1',
        description="Notch API Specification)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ghddpgml@gmail.com"),
        # license=openapi.License(name="mit"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),

    # path('app', include('app.urls')),
    path('', include('app.urls')),

    path('app/', include('allauth.urls')),
    path('app/', include('dj_rest_auth.urls')),
    path('app/', include('dj_rest_auth.registration.urls')),
    path('app/', include('app.urls')),
    # path('', loginapp.views.login, name='login'),
]

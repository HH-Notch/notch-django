# from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'toggle', views.ToggleViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('', views.base, name="base"),
    path('start/', views.start, name="start"),
    path('login/', views.start, name="login"),
    path('main/', views.start, name="main"),

    # re_path(r'^rest-auth/', include('rest_auth.urls')),
    # re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # re_path(r'^account/', include('allauth.urls')),
    # re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    path('google/login', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),

    # path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='kakao'),
    # path('rest-auth/naver/', views.NaverLogin.as_view(), name='naver'),
    # path('rest-auth/google/', views.GoogleLogin.as_view(), name='google'),
    # path('rest-auth/github/', views.GithubLogin.as_view(), name='github'),
]

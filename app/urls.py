# from allauth.account.views import confirm_email
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'goodmorning', views.GoodMorningViewSet)
# router.register(r'morningmusicname', views.MorningMusicNameViewSet, basename='morningmusicname')
router.register(r'morningmusiclist', views.MorningMusicListViewSet)
# router.register(r'morningdestname', views.MorningDestNameViewSet, basename='morningdestname')
router.register(r'morningdestlist', views.MorningDestListViewSet)
router.register(r'goodafternoon', views.GoodAfternoonViewSet)
# router.register(r'afternoonstudymusicname', views.AfternoonStudyMusicNameViewSet, basename='afternoonstudymusicname')
router.register(r'afternoonstudymusicList', views.AfternoonStudyMusicListViewSet)
# router.register(r'afternoonnapmusicname', views.AfternoonNapMusicNameViewSet, basename='afternoonnapmusicname')
router.register(r'afternoonnapmusicList', views.AfternoonNapMusicListViewSet)
router.register(r'goodevening', views.GoodEveningViewSet)
router.register(r'eveningdiary', views.EveningDiaryViewSet)
# router.register(r'eveningsleepmusicname', views.EveningSleepMusicNameViewSet, basename='eveningsleepmusicname')
router.register(r'eveningsleepmusiclist', views.EveningSleepMusicListViewSet)
router.register(r'morningblock', views.MorningBlockViewSet)
router.register(r'afternoonblock', views.AfternoonBlockViewSet)
router.register(r'eveningblock', views.EveningBlockViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('morning-blocks/', MorningBlockViewSet.as_view({'get': 'list'}), name='morning-blocks'),
    path('', views.base, name="base"),
    path('start/', views.start, name="start"),
    path('login/', views.start, name="login"),
    path('main/', views.start, name="main"),

    # re_path(r'^rest-auth/', include('rest_auth.urls')),
    # re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # re_path(r'^account/', include('allauth.urls')),

    path('google/login', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),

    # path('rest-auth/google/login', views.google_login, name='google_login'),
    # path('rest-auth/google/callback', views.google_login, name='call_back'),
    # path('rest-auth/google/finish', views.GoogleLogin.as_view(), name='google_login_todjango'),

    # path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='kakao'),
    # path('rest-auth/naver/', views.NaverLogin.as_view(), name='naver'),
    # path('rest-auth/google/', views.GoogleLogin.as_view(), name='google'),
    # path('rest-auth/github/', views.GithubLogin.as_view(), name='github'),
]

from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, ProfileView
from .router import router

urlpatterns = [

    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
         SignupView.as_view(), name='auth_signup'),

    path('user/profile/',
         ProfileView.as_view(), name='user_profile'),


     path('',include(router.urls))
]
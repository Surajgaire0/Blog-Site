from django.urls import path
from .views import SignUpView, NewPasswordResetView, NewPasswordResetCompleteView, ProfileDetail, ProfileUpdateView, \
    NewLoginView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('password_reset/',NewPasswordResetView.as_view(),name='password_reset'),
    path('reset/done/',NewPasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('update/',ProfileUpdateView.as_view(),name='profile-update'),
    #path('profile/<str:slug>/',ProfileDetail.as_view(),name='profile-detail'),
    path('login/',NewLoginView.as_view(),name='login'),
    path('profile/',ProfileDetail.as_view(),name='profile-detail')
]

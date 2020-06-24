from django.urls import path
from .views import SignUpView, NewPasswordResetView, NewPasswordResetCompleteView
#include post

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('password_reset/',NewPasswordResetView.as_view(),name='password_reset'),
    path('reset/done/',NewPasswordResetCompleteView.as_view(),name='password_reset_complete'),
    #path('',include(post.urls)),
]

from django.urls import path
from .views import SignUpView
#include post

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    #path('accounts/',),
    #path('',include(post.urls)),
]

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(),
    name='user_detail'),
    
    path('streams/', views.StreamList.as_view(), name='stream_list'),
    path('streams/<int:pk>', views.StreamDetail.as_view(),
    name='stream_detail')
]
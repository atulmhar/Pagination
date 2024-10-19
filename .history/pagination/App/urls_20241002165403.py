# users/urls.py
from django.urls import path
from .views import UserListCreateView, UserDetailUpdateDeleteView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserDetailUpdateDeleteView.as_view(), name='user_detail_update_delete'),
    path('users/<istr>/', UserDetailUpdateDeleteView.as_view(), name='user_detail_update_delete'),
]

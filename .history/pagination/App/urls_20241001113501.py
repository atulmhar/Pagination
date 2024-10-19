# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.user_list, name='user_list'),          # List all users
    path('users/create/', views.user_create, name='user_create'), # Create a new user
    path('users/<int:pk>/', views.user_detail, name='user_detail'), # Read a single user by id
    path('users/update/<int:pk>/', views.user_update, name='user_update'), # Update a user by id
    path('api/users/delete/<int:pk>/', views.user_delete, name='user_delete'), # Delete a user by id
]


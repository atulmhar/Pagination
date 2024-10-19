# urls.py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Single URL to handle all user operations
    path('users/', views.user_operations, name='user_operations'),           # List all users / Create user
    path('users/<int:pk>/', views.user_operations, name='user_operations'),  # Retrieve, update, delete a user
]


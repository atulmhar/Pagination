


from django.urls import path
from .views import UserAPIView  # Ensure this import is correct

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user_list_create'),  # List all users and create a new user
    path('users/<int:pk>/', UserAPIView.as_view(), name='user_detail_update_delete'),  # Retrieve, update, or delete a user
]



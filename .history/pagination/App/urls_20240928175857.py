# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# # from .views import UserViewSet
# from.import views
# router = DefaultRouter()
# # router.register(r'users', UserViewSet)

# urlpatterns = [

#     path('', include(router.urls)),
#     path('users/create/', views.user_create, name='user_create'), # Create a new user
#     path('users', views.user_list, name='user_list'), # Create a new user
#     path('users/<int:pk>/', views.user_detail, name='user_detail'), # Read a single user by id
#     path('users/update/<int:pk>/', views.user_update, name='user_update'), # Update a user by id
#     path('users/delete/<int:pk>/', views.user_delete, name='user_delete'), # Delete a user by id

# ]




# from django.urls import path
# from .views import user_api

# urlpatterns = [
#     path('users/', user_api, name='user_api'),  # For listing and creating users
#     path('users/<int:pk>/', user_api, name='user_detail_api'),  # For retrieving, updating, and deleting a user by ID
# ]


# from django.urls import path
# from .views import user_api  # Assuming you have combined all CRUD functionality in user_api

# urlpatterns = [
#     path('users/', user_api, name='user_list_create'),  # List all users and create a new user
#     path('users/<int:pk>/', user_api, name='user_detail_update_delete'),  # Retrieve, update, or delete a user by ID
# ]

from django.urls import path
from .views import UserAPIView  # Ensure this import is correct

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user_list_create'),  # List all users and create a new user
    path('users/<int:pk>/', UserAPIView.as_view(), name='user_detail_update_delete'),  # Retrieve, update, or delete a user
]


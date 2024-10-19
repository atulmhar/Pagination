from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
import views
router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('api/users/create/', views.user_create, name='user_create'), # Create a new user
    path('api/users/<int:pk>/', views.user_detail, name='user_detail'), # Read a single user by id
    path('api/users/update/<int:pk>/', views.user_update, name='user_update'), # Update a user by id
    path('api/users/delete/<int:pk>/', views.user_delete, name='user_delete'), # Delete a user by id

]



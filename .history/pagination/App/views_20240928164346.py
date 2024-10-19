from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .pagination import CustomUserPagination  # Import your custom pagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomUserPagination  # Use the custom pagination class

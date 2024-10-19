from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()

    serializer_class = UserSerializer


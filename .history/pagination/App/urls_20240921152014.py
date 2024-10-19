from django.urls import path
from .views import EmployeeViewSet

urlpatterns = [
    path('Employee/', EmployeeViewSet.as_view(), name='record-list'),
]

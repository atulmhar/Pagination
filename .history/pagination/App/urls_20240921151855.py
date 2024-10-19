from django.urls import path
from .views import RecordListView

urlpatterns = [
    path('EmployeeViewSet/', EmployeeViewSet.as_view(), name='record-list'),
]

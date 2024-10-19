from django.urls import path
from .views import RecordListView

urlpatterns = [
    path('Employee/', EmployeeViewSet.as_view(), name='record-list'),
]

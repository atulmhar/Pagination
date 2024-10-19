from django.urls import path
from .views import RecordListView

urlpatterns = [
    path('records/', EmployeeViewSet.as_view(), name='record-list'),
]

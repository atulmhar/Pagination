from django.urls import path
from .views import RecordListView

urlpatterns = [
    path('records/', RecordListView.as_view(), name='record-list'),
]

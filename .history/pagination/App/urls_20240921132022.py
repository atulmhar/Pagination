from django.urls import path
from . import views

# urls.py
from django.urls import path
from .views import RecordListView

urlpatterns = [
    path('records/', RecordListView.as_view(), name='record-list'),
]

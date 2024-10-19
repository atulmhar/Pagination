# views.py
from rest_framework.generics import ListAPIView
from .models import Record
from .serializers import RecordSerializer
from rest_framework.pagination import LimitOffsetPagination

class RecordListView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = LimitOffsetPagination  # Use LimitOffsetPagination

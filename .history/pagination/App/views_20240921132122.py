from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 50  # Customize page size
    page_size_query_param = 'page_size'
    max_page_size = 1000

class RecordListView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = CustomPagination  # Use custom pagination

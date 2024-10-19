from rest_framework.pagination import PageNumberPagination

class CustomUserPagination(PageNumberPagination):
    page_size =   # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 0

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.pagination import PageNumberPagination
from .models import User
from .serializers import UserSerializer

# class UserPagination(PageNumberPagination):
#     page_size =  100 # Number of users per page
#     page_size_query_param = 'page_size'  # Allow clients to set page size
#     max_page_size = 100  # Maximum page size

class UserAPIView(APIView):
    pagination_class = UserPagination  # Use custom pagination class

    def get(self, request, pk=None):
        if pk:  # Retrieve a single user if pk is provided
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:  # List all users with pagination
            users = User.objects.all()
            paginator = self.pagination_class()  # Instantiate the paginator
            paginated_users = paginator.paginate_queryset(users, request)
            serializer = UserSerializer(paginated_users, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        # CREATE a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

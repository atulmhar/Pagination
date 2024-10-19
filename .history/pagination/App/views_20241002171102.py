# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
     # Manually apply pagination
        paginator = PageNumberPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    


    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserByNameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, name):# Retrieve all users with the given name
        users = User.objects.filter(first_name=name)  # Assuming 'username' is the field for the user's name
        
        # Use `get_list_or_404` to handle the case where no users are found
        if not users.exists():
            return Response({'detail': 'No users found with this name.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
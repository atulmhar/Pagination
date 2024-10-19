# from rest_framework import viewsets
# from .models import User
# from .serializers import UserSerializer
# from .pagination import CustomUserPagination  # Import your custom pagination
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# # from .serializers import BookSerializer



# # class UserViewSet(viewsets.ModelViewSet):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# #     pagination_class = CustomUserPagination  # Use the custom pagination class


# # CREATE a new user
# @api_view(['POST'])
# def user_create(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # READ (List) all users
# @api_view(['GET'])
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# # READ (Retrieve) a single user by id
# @api_view(['GET'])
# def user_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# # UPDATE a user by id
# @api_view(['PUT'])
# def user_update(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # DELETE a user by id
# @api_view(['DELETE'])
# def user_delete(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializers import UserSerializer

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def user_api(request, pk=None):
#     if request.method == 'GET':
#         if pk:  # Retrieve a single user if pk is provided
#             try:
#                 user = User.objects.get(pk=pk)
#                 serializer = UserSerializer(user)
#                 return Response(serializer.data)
#             except User.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:  # List all users
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data)

#     elif request.method == 'POST':
#         # CREATE a new user
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PUT':
#         # UPDATE a user by id
#         if pk is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # DELETE a user by id
#         if pk is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:  # Retrieve a single user if pk is provided
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:  # List all users
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

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

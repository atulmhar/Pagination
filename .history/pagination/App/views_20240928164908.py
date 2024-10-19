from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .pagination import CustomUserPagination  # Import your custom pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
# from .serializers import BookSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomUserPagination  # Use the custom pagination class



#@api_view(['POST'])
def User_create(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# READ (List) all books
@api_view(['GET'])
def User_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = UserSerializer(books, many=True)
        return Response(serializer.data)

# READ (Retrieve) a single book by id
@api_view(['GET'])
def User_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

# UPDATE a book by id
@api_view(['PUT'])
def User_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE a book by id
@api_view(['DELETE'])
def User_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

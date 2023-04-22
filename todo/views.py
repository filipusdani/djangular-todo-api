from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Todo, TodoCategory
from .serializers import TodoSerializer, TodoCategorySerializer

class ListCreateTodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'create success'},
                            status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                field_names.append(field_name)
            return Response({'error': f'Invalid data in {field_names}'}, status=status.HTTP_400_BAD_REQUEST)
        
class RetrieveUpdateDestroyTodoCategoryAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoCategorySerializer
    queryset = TodoCategory.objects.all()

class ListCreateTodoCategoryAPIView(ListCreateAPIView):
    serializer_class = TodoCategorySerializer
    queryset = TodoCategory.objects.all()

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'create success'},
                            status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            field_names = []
            for field_name, field_errors in default_errors.items():
                field_names.append(field_name)
            return Response({'error': f'Invalid data in {field_names}'}, status=status.HTTP_400_BAD_REQUEST)
        
class RetrieveUpdateDestroyTodoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoCategorySerializer
    queryset = TodoCategory.objects.all()
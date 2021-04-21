from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsAuthorOrReadOnly


class TodoListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def get_parent(self):
        try:
            parent_id = self.kwargs['parent_id']
        except KeyError:
            return None

        parent = get_object_or_404(Todo, id=parent_id)
        return parent

    def get_queryset(self):
        parent = self.get_parent()

        todos = Todo.objects.filter(user=self.request.user)
        if parent:
            todos = todos.filter(parent=parent)
        else:
            todos = todos.filter(parent=None)

        return todos

    def perform_create(self, serializer):
        parent = self.get_parent()

        if parent:
            serializer.save(user=self.request.user, parent=parent)
        else:
            serializer.save(user=self.request.user)


class TodoDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnly]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

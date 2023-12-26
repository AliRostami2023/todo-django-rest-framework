from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializers
from permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TodoListApiView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class TodoCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class TodoUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import TaskModel
from .serializers import TaskSerializer
# Create your views here.



class TaskCreateView(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer


class TaskListView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

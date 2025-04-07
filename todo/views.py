from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# View for listing and creating tasks
class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for retrieving, updating, and deleting tasks
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

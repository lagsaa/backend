from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView
from .models import Task
from .serializers import TaskSerializer

@method_decorator(csrf_exempt, name='dispatch')
class TaskListView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from django.urls import path
from .views import TaskListView, TaskDetailView  # Corrected the import to match the class names

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),  # For listing and creating tasks
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # For individual task actions
]

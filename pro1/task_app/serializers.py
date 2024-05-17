from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    task_created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    task_deadline = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    task_assigned_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Task
        exclude = ('task_completed_date', 'task_status')



class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateSerializer(serializers.ModelSerializer):
    task_assigned_to = serializers.HiddenField(default=serializers.CurrentUserDefault())
    task_assigned_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    task_completed_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Task
        exclude = ('task_created_by', 'task_deadline')

class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"




from rest_framework import generics, views
from .serializers import TaskCreateSerializer, TaskUpdateSerializer,TaskListSerializer,TaskDeleteSerializer
from .models import Task
from .permissions import IsManagerOrTeamLeader, IsTaskAssignedTo
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
import logging


logger = logging.getLogger('task_app')

class TaskAPI(generics.ListCreateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManagerOrTeamLeader]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskListSerializer
        return TaskCreateSerializer





class TaskDetailsAPI(generics.RetrieveUpdateAPIView):
    serializer_class = TaskUpdateSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTaskAssignedTo]

class TaskDeleteAPI(generics.DestroyAPIView):
    serializer_class = TaskDeleteSerializer
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTaskAssignedTo]


class Demo(views.APIView):
    def get(self,request):
        logger.info('hello world')
        logger.warning('abcd')
        logger.error(('error occur'))
        return Response(data="msg get")


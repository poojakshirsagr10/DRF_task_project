from django.urls import path
from .views import TaskAPI,TaskDetailsAPI,Demo,TaskDeleteAPI

urlpatterns =[
    path('tasks/', TaskAPI.as_view()),
    path('tasks/<pk>/', TaskDetailsAPI.as_view()),
    path('demo/',Demo.as_view()),
    path('task/del/<pk>/',TaskDeleteAPI.as_view())
]
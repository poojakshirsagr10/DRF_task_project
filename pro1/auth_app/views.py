from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer,User

# Create your views here.
class UserRegister(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()



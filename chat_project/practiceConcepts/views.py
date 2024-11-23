from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
# Create your views here.

class simpleDisplayToCheck(APIView):
    permission_classes = [AllowAny]#because we are not using queryset here
    def get(self, request):
        return Response({"message":"Hello to the World by Mandib GET request"},status=status.HTTP_200_OK)#status goes by default
    def post(self, request):
        return Response({"message":"POST request hello ho yo", "received_data": request.data})

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
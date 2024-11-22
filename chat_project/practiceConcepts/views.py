from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# Create your views here.

class simpleDisplayToCheck(APIView):
    permission_classes = [AllowAny]#because we are not using queryset here
    def get(self, request):
        return Response({"message":"Hello to the World by Mandib"})
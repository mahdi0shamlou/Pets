from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AnimalsSerializer
from .models import Animals

class ListAnimals(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        list_animals = Animals.objects.all()
        list_animals_serializer = AnimalsSerializer(list_animals, many=True)
        return Response(list_animals_serializer.data)

class UsersAnimlas(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response('Animals UsersAnimlas')

class AddAnimals(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response('Animals AddAnimals')

class DeleteAnimals(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response('Animals DeleteAnimals')


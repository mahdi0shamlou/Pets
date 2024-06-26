from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AnimalsSerializer, AnimalsUsersSerializer
from .models import Animals, AnimalsUsers

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
        user = request.user
        list_animals_user = AnimalsUsers.objects.filter(user=user)
        list_animals_user_serializer = AnimalsUsersSerializer(list_animals_user, many=True)
        return Response(list_animals_user_serializer.data)

class AddAnimals(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        type_animals = Animals.objects.get(name=request.data['type']).id
        data_serilizers = {
            "age":  request.data['age'],
            "name": request.data['name'],
            "user": request.user.id,
            "type": type_animals,
        }
        add_animal_user_serializer = AnimalsUsersSerializer(data=data_serilizers)
        add_animal_user_serializer.is_valid(raise_exception=True)
        add_animal_user_serializer.save()
        return Response(add_animal_user_serializer.data)

class DeleteAnimals(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response('Animals DeleteAnimals')


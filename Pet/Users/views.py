from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserData


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        return Response('{"data" : "register only with post"}')

    def put(self, request):
        return Response('{"data" : "register only with post"}')

    def delete(self, request):
        return Response('{"data" : "register only with post"}')
# Create your views here.


class UsersList(APIView):
    """
    This is just test for an seriaillzer
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        all = UserData.objects.all()
        serializer = UserSerializer(all, many=True)
        return Response(serializer.data)


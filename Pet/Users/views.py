from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response


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

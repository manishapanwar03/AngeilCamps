from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer,PersonalTokenSerializer
from rest_framework import status
# Create your views here.
from rest_framework.permissions import AllowAny
from .models import PersonalToken
from django.shortcuts import get_object_or_404


class SignUp(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    
class PersonalTokenView(APIView):
    def get(self,request):
        token = PersonalToken.objects.filter(user=request.user).first()
        serializer = PersonalTokenSerializer(token,many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        data = request.data.copy()
      
        serializer = PersonalTokenSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, pk):
        token = get_object_or_404(PersonalToken, pk=pk)
        serializer = PersonalTokenSerializer(token, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



    


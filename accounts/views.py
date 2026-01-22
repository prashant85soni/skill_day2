from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRSerializer
from .utils import send_verification_email
from .models import User
# Create your views here.
class UserregistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRSerializer
    
    def create(self, request, *args, **kwargs):
       serializer=self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       user=serializer.save()
       
       email_sent=send_verification_email(user)
       return Response({
               'user': UserRSerializer(user).data,
               'message':"User Resistered Successfully. PLZ check Your Email",
               'email_sent':email_sent
           },status=status.HTTP_201_CREATED)
           





#class CustomTokenObtainView(TokenObtainPairView):
    
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


class UserRSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    
    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"password is not matching"})
        return attrs
    
    def create(self, validated_date):
        validated_date.pop("password2")
        user=User.objects.create_user(validate_password)
        #user.save()
        return user
    
    
    class Meta:
        model=User
        fields=('username',
                'email',
                'password',
                'password2',
                'first_name',
                'last_name',
                'date_of_birth',
                'phone_number')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='email',
        'phone_number',
        'date_of_birth',
        'email_verified',
        'email_verification_token',
        'created_at',
        'updated_at'
        
        
class CustomTokenObtainPairSerilaizer(TokenObtainPairSerializer):
    def validate(self,attr):
        data=super().validate(attr)
        user=self.user
        if not user or user.email_verified==False:
            raise AuthenticationFailed(
                "Auth failed!"
            )
        
        return data
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        token['email']=user.email
        token['username']=user.username
        token['email_verified']=user.email_verified
        return token
            
        
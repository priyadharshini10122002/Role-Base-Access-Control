from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import BaseUser,BaseUserManager
from django.contrib.auth.models import Group,Permission
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=BaseUser.USER_TYPE_CHOICES)

    def validate(self, data):
        required_fields = ['first_name', 'last_name', 'username', 'password','user_type']
        try:
            for field in required_fields:
             if not data.get(field):
                raise serializers.ValidationError({field: f"This field is required."})
            if data['user_type'] not in ["admin","staff","user"]:
                raise serializers.ValidationError({'user_type': 'User should be Admin, Staff, or User'})
            exist_user=BaseUser.objects.filter(username=data['username']).exists()
            if exist_user:
                raise serializers.ValidationError({'username': 'This username is already taken by a student.'})                
        except Exception as e:
            raise serializers.ValidationError({"error": "Invalid value for field_name.","details": str(e)})

        return data   
    
    def create(self,validated_data):
        user_type = validated_data['user_type']   
        if(user_type=='admin'):
              user=  BaseUser.objects.create_superuser(**validated_data)
        elif(user_type=='staff'):
               user= BaseUser.objects.create_staffuser(**validated_data)
        elif(user_type=='user'):
               user= BaseUser.objects.create_user(**validated_data)
        else:
             print("Not a valid user")

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password=serializers.CharField(write_only=True)
    
    def validate(self, data):
        username=data.get('username')
        password = data.get('password')        
        if BaseUser.objects.filter(username=username).exists():
            user_instance=BaseUser.objects.get(username=username)   
            if not user_instance.check_password(password):
                  raise serializers.ValidationError('Password Mismatch!')
            return user_instance
        else:
              raise serializers.ValidationError('Not a Registered User!')                
        

    
    def get_jwt_token(self,data):
        user=authenticate(username=data.get('username'),password=data.get('password'))
        if not user:
            return {'message':'Invalid Credentials' ,'data':{}}    
        refresh=RefreshToken.for_user(user)
        return {'message':'Login Success!' ,
                'data':{'token':{'refresh': str(refresh),'access': str(refresh.access_token),} }
                }



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, data):
        token = data['refresh']
        if not token:
              raise serializers.ValidationError('Refresh token required !')                
        return data
    def create(self, data):
        try:
           data= RefreshToken(data['refresh']).blacklist()
        except Exception as e:
            print(e)
        return data
            
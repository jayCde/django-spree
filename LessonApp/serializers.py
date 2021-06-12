from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.exceptions import AuthenticationFailed


##Custom user serializer
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style={"input_type": "password"})
    class Meta:
        model = CustomUser
        fields = "__all__"
        # fields = ("first_name", "last_name", "username", "email", "password")

##Register Serailizer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style={"input_type": "password"})
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username", "email", "password", 
                    "gramps_title", "residence", "house_number", "date_started", 
                    "residence_description"]

    def create(self, validated_data):
        CustomUser = get_user_model()
        user = CustomUser.objects.create_user(validated_data["first_name"], 
        validated_data["last_name"], validated_data["username"], validated_data["password"])

        return user
        

        
##Login Serializer
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only = True, style={"input_type": "password"})
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username", "password"]
        read_only_fields = ("id", "first_name", "last_name")

##validator function
    def validate(self, attrs):
        username = attrs.get("username", "")
        password = attrs.get("password", "")

        user = authenticate(username=username, password=password)
        print(f"-----------------{user}------------")
        if not user:
            raise AuthenticationFailed("Hey there, are you sure you belong?")
        return{"first_name": user.first_name, "last_name": user.last_name, "username": user.username}
        

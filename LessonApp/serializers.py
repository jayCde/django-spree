from rest_framework import serializers
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style={"input_type": "password"})
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {"password" : {"write_only" : True}}
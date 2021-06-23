from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.response import Response




# Create your views here.
##user reg viewset
class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects

## login viewset
class LoginAPI(generics.CreateAPIView):
    serializer_class = LoginSerializer
    # queryset = CustomUser.objects
    http_method_names = ['post', 'head']

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


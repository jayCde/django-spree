from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet, LoginAPI


#--Displays default api view--#
router = routers.DefaultRouter()
router.register(r"register", CustomUserViewSet, "user-auth")
# router.register(r"login", LoginViewset, "user-login")


urlpatterns = [
    path('', include(router.urls) ),
    path('api/login', LoginAPI.as_view(), name="login")
]


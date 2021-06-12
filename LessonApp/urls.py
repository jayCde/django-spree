from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet


#--Displays default api view--#
router = routers.DefaultRouter()
router.register(r"register", CustomUserViewSet, "user-auth")

urlpatterns = [
    path('api/', include(router.urls) ),

]


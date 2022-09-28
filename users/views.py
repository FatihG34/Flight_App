from rest_framework import generics
from django.contrib.auth.models import User
from users.serializers import ResisterSerializer 

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResisterSerializer

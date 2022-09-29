from rest_framework import generics, status
from django.contrib.auth.models import User
from users.serializers import ResisterSerializer 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user):
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['error'] = 'User does not have token . Try again ...'
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import SongSerializer, UserSerializer, RegisterSerializer
from .models import *
from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


    
@api_view(['GET'])
def Songss(request,pk):
        song = Songs.objects.get(id=pk)
        print(song.song)
        return Response({
        "id":str(song.id),
        "name":str(song.name),
        "song": "127.0.0.1:8000/media/"+str(song.song),
        "songimage": "127.0.0.1:8000/media/"+str(song.songimage),
        "artist":str(song.artist)
        })

@api_view(['GET'])
def SongList(request):
        song= Songs.objects.all()
        serializer = SongSerializer(song,many=True)
        return Response(serializer.data)
    
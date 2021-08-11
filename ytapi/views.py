from rest_framework import generics, permissions
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import SongSerializer, UserSerializer, RegisterSerializer
from .models import *
from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer




    
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
    
from django.shortcuts import render
from .models import Question,Choice,AddPlant,Posts,Comment,Profile,humidity
from .serializers import QuestionSerializer,UserSerializer,ChoiceSerializer,AddPlantSerializer,humiditySerializer,PostsSerializer,CommentSerializer,ProfileSerializer
from rest_framework import viewsets
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.admin import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.utils import timezone
import datetime
import bluetooth
import serial

nearby_device=bluetooth.discover_devices(lookup_names=True)
s=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port=1
size=1048576
add='00:19:07:34:FE:6E'
s.connect((add,port))

data=s.recv(size).decode("utf-8")
print(data)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    now=timezone.now()
    later=timezone.now()-datetime.timedelta(days=2)
    queryset=Question.objects.filter(pub_date__range=(later,now)).order_by('-pub_date')


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    now=timezone.now()
    later=timezone.now()-datetime.timedelta(days=2)
    later_later=timezone.now()-datetime.timedelta(days=4)
    queryset=Question.objects.filter(pub_date__range=(later_later,later)).order_by('-pub_date')

class AddPlantViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class= AddPlantSerializer
    queryset=AddPlant.objects.all()
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class PostsLaterViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class= PostsSerializer
    later=timezone.now()+datetime.timedelta(hours=6)-datetime.timedelta(days=2)
    later_later=timezone.now()-datetime.timedelta(days=14)
    queryset=Posts.objects.filter(pub_date__range=(later_later,later)).order_by('-pub_date')

class PostsNowViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    serializer_class=PostsSerializer
    now=timezone.now()
    later=timezone.now()-datetime.timedelta(days=2)
    queryset=Posts.objects.all().order_by('-pub_date')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class nearbyBluetoothDevice:
    def __init__(self,device):
        self.device = device


nearbyDevice= nearbyBluetoothDevice(device=data)
n=AddPlant.objects.all()
class humidityViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer=humiditySerializer(nearbyDevice)
        json = JSONRenderer().render(serializer.data)
        return Response(json )




class ProfileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]


    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
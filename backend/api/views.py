from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.views.decorators.cache import never_cache
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from rest_framework import parsers
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from rest_framework.reverse import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from random import randint,randrange
from .algorithms import *


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.exclude(is_superuser=1)
    serializer_class = UserSerializer

    @action(detail=True, methods=['POST'],serializer_class=ProfilePicSerializer,parser_classes=[parsers.MultiPartParser],)
    def pic(self, request, pk):
        user= User.objects.get(username=pk)
        myg_user=MygUser.objects.get(user=user)
        myg_user.profile_pic= request.FILES['profile_pic']
        myg_user.save()
        serializer = UserSerializer(user)
#        if serializer.is_valid():
#            serializer.save()
        return Response(serializer.data)
        #return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @action(detail=True,methods=['get'])
    def user_login(self, request,pk=None):
        #if request.method == 'POST':
        #    username = request.data['username']
        #    password = request.data['password']
    #        user = authenticate(username=username, password=password)
    #        if user:
    #            if user.is_active:
    #                login(request,user)

#        return reverse_lazy('/api/token/',request=request)
        u=User.objects.get(username=pk)
        serializer = UserSerializer(u)
        return Response(serializer.data)
    @action(detail=True,methods=['POST'])
    def user_logout(self,request,pk=None):
        logout(request)
        return Response()

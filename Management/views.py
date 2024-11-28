from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from Management.models import News
from rest_framework import viewsets
from Management.serializers import NewsSerializer
from Authentication.models import BaseUser

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class=NewsSerializer
    queryset=News.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    

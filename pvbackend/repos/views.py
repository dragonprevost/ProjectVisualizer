from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from pvbackend.repos.serializers import RepoSerializer

class RepoViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = RepoSerializer




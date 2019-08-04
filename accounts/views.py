from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import *

class AccountLCAPI(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AccountListSerializer

class AccountRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AccountListSerializer
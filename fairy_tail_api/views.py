from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
import random

from fairy_tail_api.models import Character
from fairy_tail_api.serializers import CharacterSerializer


class CharacterView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
# Create your views here.

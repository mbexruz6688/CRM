from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializer import *

class TolovListCreateAPIView(ListCreateAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer
class TolovGetUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer
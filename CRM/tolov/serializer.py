from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import *


class TolovSerializer(ModelSerializer):
    class Meta:
        models = Tolov
        fields = '__all__'
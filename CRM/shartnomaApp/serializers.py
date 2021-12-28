from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from models import *

class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ["nom", "narx"]
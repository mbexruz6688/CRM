from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from models import *

class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ["nom", "narx"]


class UstozSerializer(ModelSerializer):
    class Meta:
        model = Ustoz
        fields = ["ism", "yosh", "tel"]


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["ism", "familiya", "sharif", "jins", "tel1", "tel2", "status"]


class ShartnomaSerializer(ModelSerializer):
    class Meta:
        model = Shartnoma
        fields = "__all__"



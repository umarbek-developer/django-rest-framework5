from rest_framework import serializers
from .models import Vazifa5


class Vazifa5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vazifa5
        fields = '__all__'

from rest_framework import serializers
from .models import mainUserCentral

class MainUserCentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainUserCentral
        fields = '__all__'
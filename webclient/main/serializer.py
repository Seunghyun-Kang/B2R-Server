from rest_framework import serializers
from .models import DailyPrice, CompanyInfo

class CompanySerializer(serializers.ModelSerializer):
    class Meta: 
        model = CompanyInfo
        fields = ('__all__')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice
        fields = ('__all__')
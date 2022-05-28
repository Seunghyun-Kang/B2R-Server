from rest_framework import serializers
from .models import DailyPrice, CompanyInfo, AllCompanies, BollingerInfo, BollingerInfoUSA,  BollingerReverseSignal, BollingerReverseSignalUSA, BollingerTrendSignal, BollingerTrendSignalUSA,TripleScreenInfo,TripleScreenInfoUSA,  TripleScreenSignal, TripleScreenSignalUSA, Momentum, TradeHistory
from .models import BollingerInfoCHINA, BollingerReverseSignalCHINA, BollingerTrendSignalCHINA
from .models import  BollingerTest1Signal, BollingerTest2Signal

class AllCompanySerializer(serializers.ModelSerializer):
    class Meta: 
        model = AllCompanies
        fields = ('__all__')

class CompanySerializer(serializers.ModelSerializer):
    class Meta: 
        model = CompanyInfo
        fields = ('__all__')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice
        fields = ('__all__')

class BollingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BollingerInfo
        fields = ('__all__')
class BollingerSerializerUSA(serializers.ModelSerializer):
    class Meta:
        model = BollingerInfoUSA
        fields = ('__all__')
class BollingerSerializerCHINA(serializers.ModelSerializer):
    class Meta:
        model = BollingerInfoCHINA
        fields = ('__all__')
class BollingerTrendSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BollingerTrendSignal
        fields = ('__all__')
class BollingerTrendSignalSerializerUSA(serializers.ModelSerializer):
    class Meta:
        model = BollingerTrendSignalUSA
        fields = ('__all__')

class BollingerTrendSignalSerializerCHINA(serializers.ModelSerializer):
    class Meta:
        model = BollingerTrendSignalCHINA
        fields = ('__all__')
class BollingerReverseSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BollingerReverseSignal
        fields = ('__all__')

class BollingerTest1SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BollingerTest1Signal
        fields = ('__all__')

class BollingerTest2SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BollingerTest2Signal
        fields = ('__all__')
class BollingerReverseSignalSerializerUSA(serializers.ModelSerializer):
    class Meta:
        model = BollingerReverseSignalUSA
        fields = ('__all__')

class BollingerReverseSignalSerializerCHINA(serializers.ModelSerializer):
    class Meta:
        model = BollingerReverseSignalCHINA
        fields = ('__all__')
class TripleScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripleScreenInfo
        fields = ('__all__')

class TripleScreenSerializerUSA(serializers.ModelSerializer):
    class Meta:
        model = TripleScreenInfoUSA
        fields = ('__all__')
class TripleScreenSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripleScreenSignal
        fields = ('__all__')

class TripleScreenSignalSerializerUSA(serializers.ModelSerializer):
    class Meta:
        model = TripleScreenSignalUSA
        fields = ('__all__')

class MomentumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Momentum
        fields = ('__all__')

class TradeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeHistory
        fields = ('__all__')
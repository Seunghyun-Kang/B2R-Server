from .models import CompanyInfo, DailyPrice
from rest_framework import viewsets, status
from .serializer import PriceSerializer, CompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanySerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = DailyPrice.objects.filter(code='000020')
    serializer_class = PriceSerializer

@api_view(['GET'])
def getCompanyByCode(request, pk):
    try:
        company = CompanyInfo.objects.get(pk = pk)
                
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialier = CompanySerializer(company)
    return Response(serialier.data)

@api_view(['GET'])
def getPriceByCode(request, pk):
    try:
        prices = DailyPrice.objects.filter(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serialier = PriceSerializer(prices, many=True)
    return Response(serialier.data)
    

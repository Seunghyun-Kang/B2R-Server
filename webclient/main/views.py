from .models import CompanyInfo, DailyPrice, AllCompanies
from rest_framework import viewsets, status
from .serializer import PriceSerializer, CompanySerializer,AllCompanySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging
from django_pandas.io import read_frame

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
        company = pd.DataFrame(list(CompanyInfo.objects.get(pk = pk)))
        company.dropna(subset=['close'])
                
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #serialier = CompanySerializer(company)
    a = {column: values[0] for column, values in company.to_dict().items(orient='list')}
    return Response(a)
    #return Response(serialier.data)

@api_view(['GET'])
def getAllCompanies(request):
    try:
        companies = pd.DataFrame(list(AllCompanies.objects.all()))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    json = df.to_json(orient='records')
    return Response(json)
    #return Response(serialier.data)

@api_view(['GET'])
def getPricesByCode(request, pk):
    try:
        prices = DailyPrice.objects.filter(pk=pk)
        df = read_frame(prices)
        df.dropna(subset=['close'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    json = df.to_json(orient='records')
    return Response(json)
    #serialier = PriceSerializer(a, many=True)
    #return Response(serialier.data)
    

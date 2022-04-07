from .models import CompanyInfo, DailyPrice, AllCompanies, BollingerInfo, BollingerTrendSignal, BollingerReverseSignal, TripleScreenInfo, TripleScreenSignal
from rest_framework import viewsets, status
from .serializer import PriceSerializer, CompanySerializer,AllCompanySerializer, BollingerSerializer, BollingerTrendSignalSerializer, BollingerReverseSignalSerializer, TripleScreenSignalSerializer, TripleScreenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging, json, datetime
from django_pandas.io import read_frame
from .modules import PortfolioOptimization as po
import pandas as pd
from functools import reduce
from.modules import GetRealTimePrices as gr

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanySerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = DailyPrice.objects.all()
    serializer_class = PriceSerializer

@api_view(['GET'])
def getCompanyByCode(request, pk):
    try:
        company = pd.DataFrame(list(CompanyInfo.objects.get(pk = pk)))
        company.dropna(subset=['close'])
                
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    a = {column: values[0] for column, values in company.to_dict().items(orient='list')}
    return Response(a)

@api_view(['GET'])
def getAllCompanies(request):
    try:
        companies = CompanyInfo.objects.all()
        serializer = CompanySerializer(companies, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

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

@api_view(['GET'])
def getOptPortfolio(request):
    try:
        rawInput = request.GET["codes"]
        codes = rawInput.split(',')
        all_data = DailyPrice.objects.filter(pk__in=codes)
        df = read_frame(all_data, fieldnames=['code', 'date', 'close'])
        
        d=[]
        for s in codes:
            d.append(df.query("(code == @s)").drop(['code'], axis='columns').set_index('date').rename( {'close':s}, axis=1))
        df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['date']), d)
        
        df_merged['date'] = pd.to_datetime(df_merged.index)
        result = po.getOptPortfolio(codes, df_merged)
        print(result)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    jsonData = result.to_json(orient='records')
    return Response(jsonData)

@api_view(['GET'])
def getBollingerByCode(request, pk):
    try:
        info = BollingerInfo.objects.filter(pk=pk)
        serializer = BollingerSerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)
    
@api_view(['GET'])
def getBollingerTrendSignal(request, pk):
    try:
        info = BollingerTrendSignal.objects.filter(pk=pk)
        serializer = BollingerTrendSignalSerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getBollingerReverseSignal(request, pk):
    try:
        info = BollingerReverseSignal.objects.filter(pk=pk)
        serializer = BollingerReverseSignalSerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['GET'])
def getTripleScerenByCode(request, pk):
    try:
        info = TripleScreenInfo.objects.filter(pk=pk)
        serializer = TripleScreenSerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getTripleScerenSignal(request, pk):
    try:
        info = TripleScreenSignal.objects.filter(pk=pk)
        serializer = TripleScreenSignalSerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getRealTimePrice(request, pk):
    try:
        price , time = gr.RealTimePrice().get_price(pk)
        data = {
        "code": pk,
        "time": time,
        "price": price
    }
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(data)

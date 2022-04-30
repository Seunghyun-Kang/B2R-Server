from .models import CompanyInfo, DailyPrice, AllCompanies, BollingerInfo, BollingerTrendSignal, BollingerReverseSignal, TripleScreenInfo, TripleScreenSignal
from .models import CompanyInfoNASDAQ, DailyPriceUSA, BollingerInfoUSA, BollingerTrendSignalUSA, BollingerReverseSignalUSA, TripleScreenInfoUSA, TripleScreenSignalUSA
from .models import CompanyInfoCOIN, DailyPriceCOIN, BollingerInfoCOIN, BollingerTrendSignalCOIN, BollingerReverseSignalCOIN, TripleScreenInfoCOIN, TripleScreenSignalCOIN
from .models import Momentum
from .models import TradeHistory

from rest_framework import viewsets, status
from .serializer import PriceSerializer, CompanySerializer,AllCompanySerializer, BollingerSerializer, BollingerTrendSignalSerializer, BollingerReverseSignalSerializer, TripleScreenSignalSerializer, TripleScreenSerializer
from .serializer import BollingerSerializerUSA, BollingerTrendSignalSerializerUSA, BollingerReverseSignalSerializerUSA, TripleScreenSignalSerializerUSA, TripleScreenSerializerUSA
from .serializer import MomentumSerializer
from .serializer import TradeHistorySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging, json
from django_pandas.io import read_frame
from .modules import PortfolioOptimization as po
from .modules import Momentum as m
import pandas as pd
from functools import reduce
from.modules import GetRealTimePrices as gr
from datetime import datetime, timedelta

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
def getAllCompanies(request, symbol):
    try:
        if(symbol == "KRX"):
            companies = CompanyInfo.objects.all()
            serializer = CompanySerializer(companies, many=True)
        elif(symbol == "NASDAQ"):
            companies = CompanyInfoNASDAQ.objects.all()
            serializer = CompanySerializer(companies, many=True)
        elif(symbol == "COIN"):
            companies = CompanyInfoCOIN.objects.all()
            serializer = CompanySerializer(companies, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getPricesByCode(request,symbol ,pk):
    try:
        if symbol == "KRX":
            prices = DailyPrice.objects.filter(pk=pk)
        elif symbol == "NASDAQ":
            prices = DailyPriceUSA.objects.filter(pk=pk)
        elif symbol == "COIN":
            prices = DailyPriceCOIN.objects.filter(pk=pk)
        df = read_frame(prices)
        df.dropna(subset=['close'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    json = df.to_json(orient='records')
    return Response(json)

@api_view(['GET'])
def getOptPortfolio(request, symbol):
    try:
        rawInput = request.GET["codes"]
        codes = rawInput.split(',')
        if symbol == "KRX":
            all_data = DailyPrice.objects.filter(pk__in=codes)
        elif symbol == "NASDAQ":
            all_data = DailyPriceUSA.objects.filter(pk__in=codes)
        elif symbol == "COIN":
            all_data = DailyPriceCOIN.objects.filter(pk__in=codes)
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
def getBollingerByCode(request, symbol, pk):
    try:
        if symbol == "KRX":
            info = BollingerInfo.objects.filter(pk=pk)
            serializer = BollingerSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = BollingerInfoUSA.objects.filter(pk=pk)
            serializer = BollingerSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = BollingerInfoCOIN.objects.filter(pk=pk)
            serializer = BollingerSerializerUSA(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)
    
@api_view(['GET'])
def getBollingerTrendSignal(request, symbol, pk):
    try:
        if symbol == "KRX":
            info = BollingerTrendSignal.objects.filter(pk=pk)
            serializer = BollingerTrendSignalSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = BollingerTrendSignalUSA.objects.filter(pk=pk)
            serializer = BollingerTrendSignalSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = BollingerTrendSignalCOIN.objects.filter(pk=pk)
            serializer = BollingerTrendSignalSerializerUSA(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getBollingerReverseSignal(request, symbol, pk):
    try:
        if symbol == "KRX":
            info = BollingerReverseSignal.objects.filter(pk=pk)
            serializer = BollingerReverseSignalSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = BollingerReverseSignalUSA.objects.filter(pk=pk)
            serializer = BollingerReverseSignalSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = BollingerReverseSignalCOIN.objects.filter(pk=pk)
            serializer = BollingerReverseSignalSerializerUSA(info, many=True)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['GET'])
def getTripleScerenByCode(request, symbol, pk):
    try:
        if symbol == "KRX":
            info = TripleScreenInfo.objects.filter(pk=pk)
            serializer = TripleScreenSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = TripleScreenInfoUSA.objects.filter(pk=pk)
            serializer = TripleScreenSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = TripleScreenInfoCOIN.objects.filter(pk=pk)
            serializer = TripleScreenSerializerUSA(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getTripleScerenSignal(request, symbol, pk):
    try:
        if symbol == "KRX":
            info = TripleScreenSignal.objects.filter(pk=pk)
            serializer = TripleScreenSignalSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = TripleScreenSignalUSA.objects.filter(pk=pk)
            serializer = TripleScreenSignalSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = TripleScreenSignalCOIN.objects.filter(pk=pk)
            serializer = TripleScreenSignalSerializerUSA(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getRealTimePrice(request, symbol, pk):
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

@api_view(['GET'])
def getLastTripleScerenSignal(request, symbol, startday, lastday):
    #today = datetime.today().strftime("%Y-%m-%d")
    start = datetime.strptime(startday, "%Y-%m-%d")
    # daybefore3 = (datetime.today() - timedelta(lastday)).strftime("%Y-%m-%d")
    last = datetime.strptime(lastday, "%Y-%m-%d")

    try:
        if symbol == "KRX":
            info = TripleScreenSignal.objects.filter(date__range=[start, last], valid='valid')
            serializer = TripleScreenSignalSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = TripleScreenSignalUSA.objects.filter(date__range=[start, last], valid='valid')
            serializer = TripleScreenSignalSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = TripleScreenSignalCOIN.objects.filter(date__range=[start, last], valid='valid')
            serializer = TripleScreenSignalSerializerUSA(info, many=True)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getLastBollingerTrendSignal(request, symbol, startday, lastday):
    today = datetime.today().strftime("%Y-%m-%d")
    start = datetime.strptime(startday, "%Y-%m-%d")
    last = datetime.strptime(lastday, "%Y-%m-%d")
    print("@@@@@@@@@@@@@@@@@@@@@@@")
    print(today)
    print(start)
    print(last)
    try:
        if symbol == "KRX":
            info = BollingerTrendSignal.objects.filter(date__range=[start, last], valid='valid')
            serializer = BollingerTrendSignalSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = BollingerTrendSignalUSA.objects.filter(date__range=[start, last], valid='valid')
            serializer = BollingerTrendSignalSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = BollingerTrendSignalCOIN.objects.filter(date__range=[start, last], valid='valid')
            serializer = BollingerTrendSignalSerializerUSA(info, many=True)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getLastBollingerReverseSignal(request, symbol, startday, lastday):
    #today = datetime.today().strftime("%Y-%m-%d")
    start = datetime.strptime(startday, "%Y-%m-%d")
    # daybefore3 = (datetime.today() - timedelta(lastday)).strftime("%Y-%m-%d")
    last = datetime.strptime(lastday, "%Y-%m-%d")
    
    try:
        if symbol == "KRX":
            info = BollingerReverseSignal.objects.filter(date__range=[start, last], valid = 'valid')
            serializer = BollingerReverseSignalSerializer(info, many=True)
        elif symbol == "NASDAQ":
            info = BollingerReverseSignalUSA.objects.filter(date__range=[start, last], valid = 'valid')
            serializer = BollingerReverseSignalSerializerUSA(info, many=True)
        elif symbol == "COIN":
            info = BollingerReverseSignalCOIN.objects.filter(date__range=[start, last], valid = 'valid')
            serializer = BollingerReverseSignalSerializerUSA(info, many=True)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

@api_view(['GET'])
def getMomentum(request, symbol, duration):
    try:
        partial_hash = str(symbol) + '_' + str(30) + '_' + str(duration)
        info = Momentum.objects.filter(hashcode__icontains=partial_hash)
        serializer = MomentumSerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(serializer.data)

@api_view(['GET'])
def getTradeHistory(request, symbol, phonenumber, duration = 365):
    today = datetime.today().strftime("%Y-%m-%d")
    lastday = (datetime.today() - timedelta(duration)).strftime("%Y-%m-%d")
    print(f"PHONE NUMBER IS : {phonenumber}")
    _id = 'kiseyno'
    try:
        info = TradeHistory.objects.filter(date__range=[lastday, today], id=_id)
        serializer = TradeHistorySerializer(info, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(serializer.data)

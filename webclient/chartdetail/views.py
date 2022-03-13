from django.shortcuts import render
from .models import DailyPrice

# Create your views here.
def index(request):
    priceInfo = DailyPrice.objects.filter(code='code')
    print(f"{priceInfo}")
    return render(request,'chartdetail/index.html', {"priceInfo": priceInfo})

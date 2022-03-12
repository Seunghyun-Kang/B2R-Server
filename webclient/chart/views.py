from django.shortcuts import render
from .models import CompanyInfo

# Create your views here.
def index(request):
    company = CompanyInfo.objects.all()
    return render(request,'chart/index.html', {"company": company})
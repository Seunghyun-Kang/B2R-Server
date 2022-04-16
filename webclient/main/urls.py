from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('company', views.CompanyViewSet)
# router.register('prices', views.PriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('companylist/', views.getAllCompanies),
    path('prices/<str:pk>/', views.getPricesByCode),
    path('company/<str:pk>/', views.getCompanyByCode),
    path('optimalportfolio/', views.getOptPortfolio),
    path('bollinger/<str:pk>/', views.getBollingerByCode),
    path('bollinger_trend/<str:pk>/', views.getBollingerTrendSignal),
    path('bollinger_reverse/<str:pk>/', views.getBollingerReverseSignal),
    path('triplescreen/<str:pk>/', views.getTripleScerenByCode),
    path('triplescreen_signal/<str:pk>/', views.getTripleScerenSignal),
    path('realtime_price/<str:pk>/', views.getRealTimePrice),
    path('last3_signal_trend/', views.getLast3BollingerTrendSignal),
    path('last3_signal_reverse/', views.getLast3BollingerReverseSignal),
    path('last3_signal_triple/', views.getLast3TripleScerenSignal),
    path('latest_signal_trend/', views.getLatestBollingerTrendSignal),
    path('latest_signal_reverse/', views.getLatestBollingerReverseSignal),
    path('latest_signal_triple/', views.getLatestTripleScerenSignal),
    
]
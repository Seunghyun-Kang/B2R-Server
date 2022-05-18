from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('company', views.CompanyViewSet)
# router.register('prices', views.PriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('companylist/<str:symbol>/', views.getAllCompanies),
    path('prices/<str:symbol>/<str:pk>/', views.getPricesByCode),
    path('company/<str:pk>/', views.getCompanyByCode),
    
    path('optimalportfolio/<str:symbol>/', views.getOptPortfolio),
    
    path('bollinger/<str:symbol>/<str:pk>/', views.getBollingerByCode),
    path('bollinger_trend/<str:symbol>/<str:pk>/', views.getBollingerTrendSignal),
    path('bollinger_reverse/<str:symbol>/<str:pk>/', views.getBollingerReverseSignal),
    path('triplescreen/<str:symbol>/<str:pk>/', views.getTripleScerenByCode),
    path('triplescreen_signal/<str:symbol>/<str:pk>/', views.getTripleScerenSignal),
    
    path('realtime_price/<str:pk>/', views.getRealTimePrice),
    
    path('signal_trend/<str:symbol>/<str:startday>/<str:lastday>/', views.getLastBollingerTrendSignal),
    path('signal_reverse/<str:symbol>/<str:startday>/<str:lastday>/', views.getLastBollingerReverseSignal),
    path('signal_triple/<str:symbol>/<str:startday>/<str:lastday>/', views.getLastTripleScerenSignal),
    path('signal_test1/<str:symbol>/<str:startday>/<str:lastday>/', views.getLastBollingerTest1Signal),
    path('signal_test2/<str:symbol>/<str:startday>/<str:lastday>/', views.getLastBollingerTest2Signal),
    
    path('momentum/<str:symbol>/<int:duration>/', views.getMomentum),   
    path('trade_history/<str:symbol>/<str:phonenumber>/<int:duration>/', views.getTradeHistory)
]
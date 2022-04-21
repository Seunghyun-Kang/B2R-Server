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
    
    path('latest_signal_trend/<str:symbol>/<int:lastday>/', views.getLastBollingerTrendSignal),
    path('latest_signal_reverse/<str:symbol>/<int:lastday>/', views.getLastBollingerReverseSignal),
    path('latest_signal_triple/<str:symbol>/<int:lastday>/', views.getLastTripleScerenSignal),
    
    path('momentum/<str:symbol>/<int:lastday>/<int:stockCount>/', views.getMomentum),

]
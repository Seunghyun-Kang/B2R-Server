from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('company', views.CompanyViewSet)
# router.register('prices', views.PriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company/', views.getAllCompanies)
    path('prices/<str:pk>/', views.getPricesByCode),
    path('company/<str:pk>/', views.getCompanyByCode)
]
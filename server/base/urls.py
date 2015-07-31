from django.conf.urls import include, url
from rest_framework import routers

from . import api

router = routers.SimpleRouter()
router.register(r'companies', api.CompanyViewSet)
router.register(r'stock-prices', api.StockPriceViewSet)



urlpatterns = router.urls

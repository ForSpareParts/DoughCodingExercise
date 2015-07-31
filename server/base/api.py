from rest_framework import viewsets

from . import models, serializers


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Company.objects.all()
    serializer = serializers.CompanySerializer

class StockPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.StockPrice.objects.all()
    serializer = serializers.StockPriceSerializer

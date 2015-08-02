from rest_framework import filters, viewsets

from . import models, serializers

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    search_fields = ('name', 'symbol')


class StockPriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.StockPrice.objects.all()
    serializer_class = serializers.StockPriceSerializer

    filter_fields = ('company',)

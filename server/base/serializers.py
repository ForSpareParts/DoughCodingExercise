from rest_framework import serializers

from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ['id', 'name', 'symbol', 'exchange']

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockPrice
        fields = ['id', 'company', 'time', 'price']

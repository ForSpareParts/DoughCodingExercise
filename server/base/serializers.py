from rest_framework import serializers

from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ['name', 'price_history']

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockPrice
        fields = ['company', 'time', 'price']

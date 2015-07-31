from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=10)

class StockPrice(models.Model):
    company = models.ForeignKey(Company, related_name='price_history')
    time = models.DateTimeField()
    price = models.DecimalField(max_digits=15, decimal_places=10)

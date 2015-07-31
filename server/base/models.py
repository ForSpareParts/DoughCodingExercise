from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return "Company: " + self.name

    class Meta:
        verbose_name_plural = 'Companies'

class StockPrice(models.Model):
    company = models.ForeignKey(Company, related_name='price_history')
    time = models.DateTimeField()
    price = models.DecimalField(max_digits=15, decimal_places=10)

    def __unicode__(self):
        return "{name}: {time}: {price}".format(
            name=self.company.name,
            time=self.time,
            price=self.price)

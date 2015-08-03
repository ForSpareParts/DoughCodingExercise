from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    exchange = models.CharField(max_length=50)

    def __unicode__(self):
        return "Company: " + self.name

    class Meta:
        verbose_name_plural = 'Companies'

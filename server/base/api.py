from rest_framework import filters, viewsets

from . import models, serializers

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    search_fields = ('name', 'symbol')

from django.conf.urls import include, url
from rest_framework import routers

from . import api, views

router = routers.SimpleRouter()
router.register(r'companies', api.CompanyViewSet)



urlpatterns =  [
    url(r'companies/(?P<company_id>[^/.]+)/price-history/$',
        views.company_price_history),
    url(r'', include(router.urls))
]

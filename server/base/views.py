from datetime import date
import dateutil.parser
import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import yahoo_finance

from .models import Company

# Create your views here.

def company_price_history(request, company_id):
    start_date = request.GET.get('start_date')
    if not start_date:
        return HttpResponseBadRequest(
            "Stock price history requires a start date")

    company = Company.objects.get(pk=company_id)

    end_date = request.GET.get('end_date') or date.today().isoformat()

    share = yahoo_finance.Share(company.symbol)
    history = share.get_historical(start_date, end_date)

    dates = [item['Date'] for item in history]
    prices = [item['Close'] for item in history]

    return HttpResponse(
        json.dumps({'dates': dates, 'prices': prices}),
        content_type='application/json')

from django.shortcuts import render
from .currency_value import currency_USD,currency_EUR,currency_RUB,currency_KZT


def home(request):


    return render(request, 'index.html', {
        'USD': currency_USD, 
        'EUR': currency_EUR,
        'RUB': currency_RUB,
        'KZT': currency_KZT,
    })



def convertDollar(request):
    if int(request.POST.get('input_value')) > 0:
        input_value = int(request.POST.get('input_value'))
        converted_usd = input_value / currency_USD

    return render(request, 'index.html', {
        'USD': currency_USD, 
        'EUR': currency_EUR,
        'RUB': currency_RUB,
        'KZT': currency_KZT,
        'converted_usd_result':converted_usd,
        })

def convertDollar(request):
    if int(request.POST.get('input_value')) > 0:
        input_value = int(request.POST.get('input_value'))
        converted_usd = input_value / currency_USD
        converted_eur = input_value / currency_EUR
        converted_rub = input_value / currency_RUB
        converted_kzt = input_value / currency_KZT

    return render(request, 'index.html', {
        'USD': currency_USD, 
        'EUR': currency_EUR,
        'RUB': currency_RUB,
        'KZT': currency_KZT,
        'converted_usd_result': format(converted_usd, '.2f'),
        'converted_eur_result': format(converted_eur, '.2f'),
        'converted_rub_result': format(converted_rub, '.2f'),
        'converted_kzt_result': format(converted_kzt, '.2f')
        })



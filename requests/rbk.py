import requests
import xmltodict

nbkr_url = 'https://www.nbkr.kg/XML/daily.xml'
response = requests.get(nbkr_url)
curs_dict = xmltodict.parse(response.text)

date = curs_dict['CurrencyRates']['@Date']

print('курс валют по НБКР на', date)

for currency in curs_dict['CurrencyRates']['Currency']:
    print(currency['@ISOCode'], ':' , currency['Value'])
    if currency['@ISOCode'] == 'USD':
        print('Доллар', ':', currency['Value'])
    if currency['@ISOCode'] == 'EUR':
        print('евро', ':', currency['Value'])
    if currency['@ISOCode'] == 'KZT':
        print('тенге', ':', currency['Value'])
    if currency['@ISOCode'] == 'RUB':
        print('рубль', ':', currency['Value'])


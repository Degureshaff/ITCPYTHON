from django.shortcuts import render
import requests
import json

covid_url = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'

covid_url_all = 'https://covid-api.mmediagroup.fr/v1/cases'


def covid_status(request):
    countries_all_res = requests.get(covid_url_all)
    countries_dict = countries_all_res.json()
    countries_dict_keys = []

    for country in countries_dict.keys():
        countries_dict_keys.append(country)

    return render(request, 'index.html', {
        'country_all': countries_dict_keys
    })



def get_covid_status(request):
    country_code  = request.POST.get('country_code')
    
    covid_url_final = covid_url.format(country = country_code)
    covid_res = requests.get(covid_url_final)
    covid_dict = covid_res.json()




    countries_all_res = requests.get(covid_url_all)
    countries_dict = countries_all_res.json()
    countries_dict_keys = []

    confirmed = covid_dict['All']['confirmed']
    recovered = covid_dict['All']['recovered']
    deaths = covid_dict['All']['deaths']

    


    for country in countries_dict.keys():
        countries_dict_keys.append(country)


    return render(request, 'index.html',{
        'country_code':country_code,
        'confirmed': confirmed,
        'recovered': recovered,
        'deaths': deaths,
        'countries_all': countries_dict_keys
    })


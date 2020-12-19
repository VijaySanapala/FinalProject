from django.shortcuts import render

from django.http import HttpResponse

import json
import requests
from .models import covid19


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
# def time(request):
#     for i in range(0, len(time)):
#         working_dict = {}
#         working_dict['Date'] = time[i]
#         for key in col_names:
#             working_dict[key] = dict_data[key][i]
#         print('Daywise',i,working_dict)
#         row = covid19()

#         row.Date = datetime.utcfromtimestamp(working_dict['Date'])
#         #row.index = i + 1
#         row.NewConfirmed = working_dict['NewConfirmed']
#         row.TotalConfirmed = working_dict['TotalConfirmed']
#         row.NewDeaths = working_dict['NewDeaths']
#         row.TotalDeaths = working_dict['TotalDeaths']
#         row.NewRecovered = working_dict['NewRecovered']
#         row.TotalRecovered = working_dict['TotalRecovered']
#         row.Country = working_dict['Country']
#         row.CountryCode = working_dict['CountryCode']
#         row.Slug = working_dict['Slug']
#         row.NewDeaths = working_dict['NewDeaths']
#         row.save()
        
def getdata(request):
    url = 'https://api.covid19api.com/summary'

    response = requests.get(url, headers={"content-type":"text"})
    data = json.loads(response.text)

    for i in range(0,len(data['Countries'])):
        row = covid19()

        row.Date = (data['Countries'][i]['Date'])
        row.Index = i + 1
        row.Country = (data['Countries'][i]['Country'])
        row.TotalDeaths= (data['Countries'][i]['TotalDeaths'])
        row.NewDeaths= (data['Countries'][i]['NewDeaths'])
        row.NewRecovered= (data['Countries'][i]['NewRecovered'])
        row.TotalRecovered= (data['Countries'][i]['TotalRecovered'])
        row.CountryCode= (data['Countries'][i]['CountryCode'])
        row.Slug= (data['Countries'][i]['Slug'])
        row.NewConfirmed= (data['Countries'][i]['NewConfirmed'])
        row.TotalConfirmed= (data['Countries'][i]['TotalConfirmed'])
        row.NewDeaths= (data['Countries'][i]['NewDeaths'])
        row.save()
        
    return HttpResponse("Congrats!")

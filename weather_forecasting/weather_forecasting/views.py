from django.http import HttpResponse
from django.shortcuts import render
import requests
import os
from datetime import datetime
# def home(request):
#     data={
#         "title":"TO_DO_APP",
#         "list":["poonam","pooja","prachi"],
#         "numbers":[2,3,4,6,90]
#     }
#     return render(request,"check.html",data)

def home(request):
    return render(request, 'home.html')

def proceed(request):
    return render(request, 'check.html')


def process_form(request):
    if request.method == 'POST':
        name = request.POST.get('city_name')  # Get the value of the 'name' input field
        # processed_value=name.upper()
        # Do something with the input data
        # For example, you could pass it to another function or save it in a database
        user_api = '3898cb6a0215bc4cdab0a54cfd827d1a'
        location = name

        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        #create variables to store and display data
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print ("-------------------------------------------------------------")
        print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        print ("-------------------------------------------------------------")

        print ("Current temperature is: {:.2f} deg C".format(temp_city))
        print ("Current weather desc  :",weather_desc)
        print ("Current Humidity      :",hmdt, '%')
        print ("Current wind speed    :",wind_spd ,'kmph')
        data={
            "name":name,
            "temp":temp_city,
            "desc":weather_desc,
            "humidity":hmdt,
            "speed":wind_spd
        }
        return render(request, 'result.html',data)
        # return HttpResponse("this is about us page")
    return render(request, 'check.html')
    
    
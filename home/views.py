import requests
from django.shortcuts import render


def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8fc1bb7939c21d3e79b02852cd3d6e79'
    if request.method=='POST':
        city=request.POST['city']
    #city='las vegas'
        r=requests.get(url.format(city)).json()

        city_weather={
            'city': city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        contex ={'city_weather':city_weather}

        return render(request,'mm.html',contex)
    else:
        return render(request,'mm.html')

# Create your views here.

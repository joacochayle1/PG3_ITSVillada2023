import requests
from django.shortcuts import render


API_KEY = '88ee208bd0104304ad4110850240706'

def weather_view(request):
    
    city = request.GET.get('city', 'London')  
    
    
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}')
    data = response.json()

   
    weather_data = {
        'city': data.get('location', {}).get('name'),
        'region': data.get('location', {}).get('region'),
        'country': data.get('location', {}).get('country'),
        'temperature_c': data.get('current', {}).get('temp_c'),
        'humidity': data.get('current', {}).get('humidity'),
        'condition': data.get('current', {}).get('condition', {}).get('text'),
        'icon': data.get('current', {}).get('condition', {}).get('icon')
    }

    return render(request, 'weather/index.html', {'weather_data': weather_data})

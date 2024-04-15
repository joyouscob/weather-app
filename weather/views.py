from django.shortcuts import render
from .models import WeatherHistory
from .serializers import WeatherHistorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def home(request):
    # try:
    weather = WeatherHistory.objects.all().order_by('-id')[:10]
    weatherd = WeatherHistorySerializer(weather, many=True)
    return Response({"weather":weatherd.data}, status=status.HTTP_200_OK)
    # except:
        # return Response({"message":"There was an error displaying data"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_weather_data(request):
    try:
        '''
                {
                    "location":"Abuja",
                    "temperature": "23.4",
                    "weather_description": "Sunny or rainy",
                    "latitude": "23.45",
                    "longitude": "34.34",
                    "date_data": "24th July, 2024",
                    "humidity":  "23.45",
                    "real_feel": "23.45",
                    "wind_speed": "1.3",
                    "sun_rise": "6:56AM",
                    "sun_set": "6:40PM",
                    "max_temp": "23.4",
                    "min_temp": "23.4",
                    "weather_data": "dump json",
                    "forecast_data": "dump json"
                }
        '''
        data = request.data
        print(data)
        weather_info = WeatherHistory.objects.create(**data)
        weather = WeatherHistory.objects.all().order_by('-id')[:10]
        print(weather)
        weather = WeatherHistorySerializer(weather, many=True)
        return Response(weather.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"info":e}, status=status.HTTP_400_BAD_REQUEST)

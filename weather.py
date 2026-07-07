import requests
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n*** Get Weather Conditions ***\n')

    city = input("\n Please Enter the City name => \n")


    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=celsius'

    # print(request_url)
    weather_data = requests.get(request_url).json()

    # pprint(weather_data)
    print(f'\nCurrent weather for {weather_data["name"]} is {weather_data["weather"][0]["description"]} \n')
    print(f'\nThe Temp is {weather_data["main"]["temp"]}°C\n')
    print(f'\nThe feels like is {weather_data["main"]["feels_like"]}°C \n')
    

if __name__ == "__main__":
    get_current_weather()
     


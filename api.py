import json
import requests
city_name=input('Enter a city name:')
api_key='20ae735361f917113a87c1ed412ec3af'
api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
get_server_info=requests.get(api_url)
json_data=get_server_info.json()
pretty_data=json.dumps(json_data,indent=4)
print(pretty_data)
D=json_data["weather"][0]['description']

T=json_data['main']['temp']

print(f'The current weather Description is:{D} & Temperature is :{T}')
import requests
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "3710d9cfd0b6e6b895b9ebaca3a9be3e"
account_sid = "AC5fa6c5a6eb0469ffa205f93d360898f4"
auth_token = "533ee0c3d029a4b23806b2991338307f"

parameters = {
    "lat": 38.847118,
    "lon": -77.306320,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
# print(weather_data)
hourly_data = weather_data["hourly"]
will_rain = False

for x in hourly_data[:12]:
    hourly_forecast = x["weather"][0]["id"]
    # print(hourly_forecast)
    if hourly_forecast < 700:
        will_rain = True

client = Client(account_sid, auth_token)
if will_rain:
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_="+14422410317",
        to="+16078787777"
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body="It's not raining today.",
        from_="+14422410317",
        to="+16078787777"
    )
    print(message.status)


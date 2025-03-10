import json
import requests


if __name__ == '__main__':
    city = "Krasnoyarsk"
    api = "b13aa5f80dcd0061f8aabe996268fbbe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

    req = requests.post(url)
    res = json.loads(req.text)

    if req.status_code == 200:

        weather = res['weather'][0]['description']
        humidity = res['main']['humidity']
        pressure = res['main']['pressure']
        print(f"Weather in {city}")
        print(f"Description: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure}hPa")

    else:
        print("No Data")
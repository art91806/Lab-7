import json
import requests


if __name__ == '__main__':
    
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)


    if res.status_code == 200:

        data = res.json()
        x = data["iss_position"]["latitude"]
        y = data["iss_position"]["longitude"]

        print(f"МКС в настоящее время находится в:")
        print(f"Широта: {x}, Долгота: {y}\n")
        
    else:
        print("Ошибка при получении текущего местоположения МКС:", res.status_code)

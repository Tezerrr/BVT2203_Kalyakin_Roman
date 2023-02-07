import requests
import datetime

now_date = ".".join(map(str, (map(int, str(datetime.date.today()).split("-")[1:]))))
s_city = "Moscow,RU"
appid = "3b3d76999b834fb8b84d49c4e8f809a1"
req = requests.get(f"http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
req1 = requests.get(f"http://api.openweathermap.org/data/2.5/forecast",
                    params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = req.json()
data1 = req1.json()

print(f'Видимость на сегодня({now_date}) = {data["visibility"]}')
print(f'Скорость ветра на сегодня({now_date}) = {data["wind"]["speed"]}')

vis = list(i["visibility"] for i in data1["list"])
speed = list(i["wind"]["speed"] for i in data1["list"])
# На неделю получаем 40 значений
print(f'Видимость на неделю = {min(vis)} - {max(vis)}, среднее = {sum(vis) / 40}')
print(f'Скорость ветра на неделю = {min(speed)} - {max(speed)}, среднее = {sum(speed) / 40}')
print(f'Видимость на неделю = {min(vis)} - {max(vis)}, среднее = {sum(vis) / 40}')
print(f'Скорость ветра на неделю = {min(speed)} - {max(speed)}, среднее = {sum(speed) / 40}')
print("Точный прогноз погоды на неделю:")
for i in data1['list']:
    print("Дата <", i['dt_txt'], "> \r\n"
                                 f"Видимость <{i['visibility']}> \r\nПогодные условия <",
          i['wind']['speed'], ">")
    print("____________________________")

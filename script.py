import requests,re

city=input("Введите название города.\n")
my_id=input("Введите свой API id\n")

def get_city_id(city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': city_name, 'type': 'like', 'units': 'metric'
                             , 'lang': 'ru', 'APPID': my_id})
        data = res.json()
        city_id = data['list'][0]['id']
        print('ID города-', city_id)
    except Exception as e:
        pass
    city_id=int(city_id)
    return city_id

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'id': get_city_id(city), 'units': 'metric'
                                , 'lang': 'ru', 'APPID': my_id})
    data = res.json()
    avg_temp=0
    counter=0
    max_temp=-90 
    for i in data['list']:
        match = re.search(r'\d+:\d+:\d+', i['dt_txt'])
        hour=int(match[0].split(":")[0])
        if 5<=hour<=12:
                temp=int('{0:+3.0f}'.format(i['main']['temp']))
                avg_temp+=temp
                counter+=1
                if (max_temp<temp):
                        max_temp=temp       
except Exception as e:
    pass


avg_temp/=counter
print("\nСредняя утренняя температура-"
      ,f"{avg_temp:.2f}"
      ,"\nМаксимальная утренняя температура-",max_temp)

input('\nDone')

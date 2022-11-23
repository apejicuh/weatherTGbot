import requests

# s_city = "Saint Petersburg, RU"
# city_id = 498817
appid = "7fa728f8630ead5b65bceadfbbff0615"

# Прогноз
def request_forecast():
    forecast_str = ''
    city_id = 498817

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        
        count = 0
        for i in data['list']:
            forecast_str += ( (i['dt_txt'])[5:16] + '{0:+3.0f}'.format(i['main']['temp']) + ' ' + 
                   i['weather'][0]['description'] + '\n')
            if count == 4:
                break
            else:
                count += 1
    except Exception as e:
        print("Exception (forecast):", e)
        pass
    
    return forecast_str
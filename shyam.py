url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
import urllib.request
import json

data = urllib.request.urlopen(url).read()
data = json.loads(data)
data = data["list"]
while True:
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    try:
        inp_key = int(input ("please enter the input number : "))
    except:
        print("wrong input: please try again")
        continue
    if inp_key == 0 :
        print('exiting program')
        break
    inp_date = input("print date in format YYYY-MM-DD : ")
    data_of_date = [row for row in data if row["dt_txt"].split(" ")[0]==inp_date]
    if inp_key == 1:
        temp = [row['main']['temp'] for row in data_of_date]
        print(f'temp is {temp}')
    elif inp_key == 2:
        wind_speed = [row["wind"]["speed"] for row in data_of_date]
        print(f"wind speed is {wind_speed}")
    elif inp_key==3:
        pressure = [row["main"]["pressure"] for row in data_of_date]
        print(f"pressure is {pressure}")
    else:
        print("wrong key : please check your input ")



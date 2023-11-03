from datetime import datetime
import requests # package

# Parameter
APPID = "6ff342d55711e417457cf5c537e3311d"
CITY = "Jakarta "

# saya mengambil url dari (5 day / 3 hour)
url = f"http://api.openweathermap.org/data/2.5/forecast?appid={APPID}&q={CITY}&units=metric"

response = requests.get(url).json()

time = "12:00:00" # hanya mengambil ramalan cuaca pada jam 12:00:00

output = f"Weather Forecast:\n" #Header

for forecast in response["list"]:
    date_time = forecast["dt_txt"]
    
    if time in date_time:
        temperature = forecast["main"]["temp"]
        
        date = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        date_format = date.strftime("%a, %d %b %Y")
        
        output += f"{date_format}: {temperature}°C\n"

print(output)
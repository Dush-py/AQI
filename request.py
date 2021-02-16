import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'PM2.5':2, 'PM10':9, 'NO':6,'NO2':12,'NOx':11,'NH3':5,'CO':4,'SO2':12,'O3':9,'Benzene':8,'Toluene':8,'Xylene':6})

print(r.json())

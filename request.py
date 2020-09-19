import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sepallength':2.1, 'sepalwidth':2.4, "petallength":6.3 , "petalwidth":5.0})

print(r.json())
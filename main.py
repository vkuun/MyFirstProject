import requests
import datetime
response = requests.get('https://google.com')
print("status of code answer:", response.status_code)
print("Length of answer:",len(response.text))
print("Текущая дата:", datetime.datetime.now())
import json

import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)
token = (response.json()['token'])
sec = (response.json()['seconds'])
# print(token)
# print(sec)

response2 = requests.get(url, params={"token": token})
if response2.text == '{"status":"Job is NOT ready"}':
    print("Correct status: Job is NOT ready")
else:
    print("Incorrect status")
# print(response2.text)

import time
time.sleep(sec)

response3 = requests.get(url, params={"token": token})
if "result" and '"status":"Job is ready"' in response3.text:
    print("Have result, Job is ready")
else:
    print("No result or job isn`t ready")


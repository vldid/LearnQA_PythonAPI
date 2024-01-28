import requests

#responseGET = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
#print(responseGET.text)

#responsePUT = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
#print(responsePUT.text)

#responsePOST = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
#print(responsePOST.text)

#responseDELETE = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
#print(responseDELETE.text)

#1
#responseNoMethod = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
#print(responseNoMethod.text)   #Wrong method provided

#2
#responseHEAD = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
#print(responseHEAD.text)       #В ответе пусто

#3
#responseGET = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
#print(responseGET.text)        #В ответе {"success":"!"}

#4
methods = ["get", "put", "post", "delete"]
params = [{"method": "GET"},
          {"method": "PUT"},
          {"method": "POST"},
          {"method": "DELETE"}]
param_types = ["params", "data"]

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

for method in methods:
    for param in params:
        for param_type in param_types:
         
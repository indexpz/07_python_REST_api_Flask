import requests
from requests import delete

BASE = "http://127.0.0.1:5000/"

# response = requests.post(BASE + "helloworld")
# print(response.json())


# response = requests.get(BASE + "helloworld/ala")
# print(response.json())
#
# response = requests.get(BASE + "helloworld/bill")
# print(response.json())


# response = requests.put(BASE + "video/3", {"likes": 10, "name": "Ala", "views": 10000})
# print(response.json())
# input()
# response = requests.get(BASE + "video/6", )
# print(response.json())

data = [{"likes": 10, "name": "Ala", "views": 10000},
		{"likes": 20, "name": "Bala", "views": 20000},
		{"likes": 30, "name": "Cala", "views": 30000}]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())

# input()
# response = requests.delete(BASE + 'video/0')
# print(response)
# input()
# response = requests.get(BASE + "video/2")
# print(response.json())

import requests as re

api = "https://www.breakingbadapi.com/api/characters/"
data = [];

for i in range (1,58):
	try:
		response = re.get(api+str(i))
		data.append(response.json()[0])
	except:
		print(f'Error on i= {i}')

print(data)
with open ("results.txt","w") as f:
	f.write(data)
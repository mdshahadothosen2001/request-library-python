import pip._vendor.requests

#Here some issue for import requests so use pip,_vendor.requests
data = pip._vendor.requests.get('http://127.0.0.1:8000/')

print(data.status_code)
print("BEG  display status:",data,"END",sep='\n')

print("BEG1 display all dir:",dir(data),"END1",sep='\n')

print('BEG2 display only text',data.text,'END',sep='\n')

print(data.url)

print(dir(data))

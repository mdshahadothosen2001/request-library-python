import pip._vendor.requests

payload={'username':'admin','password':'testing'}
#here should have created post api then
# we can post data from here
datalist=pip._vendor.requests.post('http://httpbin.org/post',data=payload)

print(datalist)
print(datalist.text)
print(dir(datalist))
print('Display data as a dictionary')
dict=datalist.json()
print(dict['form'])
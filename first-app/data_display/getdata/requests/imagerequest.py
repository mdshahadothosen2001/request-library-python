import pip._vendor.requests

#where image in web app
data = pip._vendor.requests.get('https://imgs.xkcd.com/comics/python.png')

#image-name.image-type
print(data)
with open('temp.png', 'wb') as f:
    f.write(data.content)
# see project folder this image because use file management
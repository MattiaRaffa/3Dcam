import json
from urllib import request
import imageio
import cv2

#get image 1
cam = cv2.VideoCapture(0)

while True:
	ret, image = cam.read()
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
cv2.imwrite('/home/pi/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()

#get image 2
cam = cv2.VideoCapture(1)

while True:
	ret, image = cam.read()
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
cv2.imwrite('/home/pi/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()

#gifname
a=1
num=a++
GIFname= str('/gif/movie'+ num+ '.gif')

#gif creation
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(GIFname, images)

#upload
url = "http://upload.giphy.com/v1/gifs"

values = {
  "api_key": "FOX6LhbsIIRlGeAsBFHHJpk7dTMid2uF",
  "username": "CasermaPassalacqua",
  "file": GIFname,
  "tags": "3Dcam,nòva,novara",
}

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
}

data = json.dumps(values).encode("utf-8")

req = request.Request(url, data, headers)
with request.urlopen(req) as res:
  print(res.read().decode())
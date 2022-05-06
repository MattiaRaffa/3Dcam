def cap(l):
	for l in [0,1]:
		cam = cv2.VideoCapture(l)

		while True:
			ret, image = cam.read()
			cv2.imshow('Imagetest',image)
			k = cv2.waitKey(1)
			if k != -1:
				break
		cv2.imwrite('/home/pi/'+l+'.jpg', image)


import cv2
import numpy as np
from skimage.io import imread
from flask import Flask

app = Flask(__name__)

@app.route('/')
def css():
	lowerBound=np.array([55,60,0])
	upperBound=np.array([90,200,255])
	cam= cv2.imread('home.JPg')
	img=cv2.resize(cam,(340,220))
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(imgHSV,lowerBound,upperBound)
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(imgHSV,lowerBound,upperBound)
	ratio_white = cv2.countNonZero(mask)/(img.size/3)
	c=np.round(ratio_white*100, 2)
	print('mangrove percentage:', np.round(ratio_white*100, 2))
	#cv2.imshow("mask",mask)
	#cv2.imshow("cam1",img)
	cv2.imwrite("after.jpg",mask)
	cv2.waitKey(80)
	return "HEELO"

if __name__ == '__main__':
    app.run()

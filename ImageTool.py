from PIL import Image
import numpy as np
class ImageTool:
	def __init__(self):
		pass
	def Binarization(self,im,th = None):
		h,w = im.shape
		if(th == None):
			sum = 0
			for i in im:
				for j in i:
					sum += j
			th = int(sum/(h*w))
		for i in range(h):
			for j in range(w):
				if(im[i][j]>=th):
					im[i][j] = 255
				else:
					im[i][j] = 0
		return im
	def ImageSave(self,fp,im):
		if(im.dtype != "uint8"):
			Image.fromarray(im.astype("uint8")).save(fp)
		else:
			Image.fromarray(im).save(fp)

	def Sobel(self,im):
		im = im.astype("int16")
		h,w = im.shape
		im_new = im*1
		for i in range(1,h-1):
			for j in range(1,w-1):
				a = im[i-1][j-1]
				b = im[i-1][j]
				c = im[i-1][j+1]
				d = im[i][j-1]
				e = im[i][j]
				f = im[i][j+1]
				g = im[i+1][j-1]
				h = im[i+1][j]
				k = im[i+1][j+1]
				Gx = (g+2*h+k)-(a+2*b+c)
				Gy = (c+2*f+k)-(a+2*d+g)
				im_new[i][j] = int(((Gx**2)+(Gy**2))**(0.5))
		return im_new.astype("uint8")
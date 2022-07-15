from matplotlib import pyplot as plt
import cv2, numpy as np

def show(im):
	plt.imshow(im)
	plt.show()

# im = Image.open("out copy.jpg")
im = cv2.imread("out copy.jpg")
h, w, c = im.shape

rs = np.zeros((304, 92, 3), dtype=np.int16)

for k, i in enumerate(range(0, w, 92)):
	rs[k] = im[0][i:i+92]

rs = cv2.flip(rs, 0)
rs = cv2.rotate(rs, cv2.cv2.ROTATE_90_CLOCKWISE)
show(rs)
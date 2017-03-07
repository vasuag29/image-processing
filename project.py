import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample_img.png',0)
cv2.waitKey(0)
cv2.destroyAllWindows()
avg = cv2.blur(img,(5,5))
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

filter1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
filter2 = np.array([[-1, 0, -1], [0, 4, 0], [-1, 0, -1]])

hvd = cv2.filter2D(img, -1, filter1)
dd = cv2.filter2D(img, -1, filter2)

plt.subplot(2,3,1),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(2,3,2),plt.imshow(avg, cmap='gray'),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray'),plt.title('Sobel X')
plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray'),plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(hvd,cmap = 'gray'),plt.title('Horizontal-Vertical Diff')
plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(dd,cmap = 'gray'),plt.title('Diagonal Diff')
plt.xticks([]), plt.yticks([])
plt.show()

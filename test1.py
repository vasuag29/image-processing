import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample_img.png',0)
cv2.waitKey(0)
cv2.destroyAllWindows()

filter1 = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
filter2 = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

sobelx = cv2.filter2D(img, -1, filter1)
sobely = cv2.filter2D(img, -1, filter2)

plt.subplot(1,2,1),plt.imshow(sobelx, cmap='gray'),plt.title('Sobelx')
plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(sobely, cmap='gray'),plt.title('Sobely')
plt.xticks([]), plt.yticks([])
plt.show()

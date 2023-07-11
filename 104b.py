#crate image using arrays
import numpy as np
import cv2
black=np.zeros([600,600])
cv2.imshow("black image",black)
cv2.waitKey(0)
print(black)
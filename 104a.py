import cv2
img=cv2.imread("poster.jpg")

# coverting the color img to greyscale img
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale",gray_img)
cv2.waitKey(0)
print(img)


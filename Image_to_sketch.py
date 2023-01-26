Importing Libraries
import cv2
import matplotlib.pyplot as plt
Reading the Image
img = cv2.imread('test.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_imgb_img);
plt.show()
# cv2.imshow("test",img)
# cv2.waitKey(0)
Converting image to Gray color
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grey_rgb_img = cv2.cvtColor(grey_img, cv2.COLOR_BGR2RGB)
plt.imshow(grey_rgb_img)
Inverting the image
invert_img = cv2.bitwise_not(grey_img)
inv_rgb_img = cv2.cvtColor(invert_img, cv2.COLOR_BGR2RGB)
plt.imshow(inv_rgb_img)
Bluring the image
blur_img = cv2.GaussianBlur(invert_img,(25,25),0)
blur_rgb_img = cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB)
plt.imshow(blur_rgb_img)
Inverting and Bluring image
inv_blur_img = cv2.bitwise_not(blur_img)
inv_blur_rgb_img = cv2.cvtColor(inv_blur_img, cv2.COLOR_BGR2RGB)
plt.imshow(inv_blur_rgb_img)
Converting to sketch
sketch_img = cv2.divide(grey_img,inv_blur_img,scale=256.0)
sketch_rgb_img = cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(sketch_rgb_img)
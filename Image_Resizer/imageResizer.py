import cv2

img = cv2.imread("Python-Projects\image.jpeg", cv2.IMREAD_UNCHANGED)
print(type(img))
print("Original Dimensions : ", img.shape)
print("Image Type : ", img.dtype)

scale_percent = 50  # percent of original size
height = int(img.shape[0] * scale_percent / 100)
width = int(img.shape[1] * scale_percent / 100)

resized_img = cv2.resize(img, (width, height))

cv2.imwrite("Python-Projects\Resized_image.png", resized_img) # Uncomment the above line to save the resized image

# Display the resized image
# cv2.imshow("Image", img)
# cv2.waitKey(0)
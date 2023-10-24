import cv2

image = cv2.imread('Images/people1.jpg')
print(image.shape)

imagem = cv2.resize(image, (800, 600))

image_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
print(image_gray.shape)


cv2.imshow('WindowTest', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Libraries
OpenCV
Dlib
TensorFlow
Darknet
Caffe framework

drive.google.com/drive/folders/1fnn6e8q7Ykp7nqOPWGeSiijlNTt_kkPL
'''
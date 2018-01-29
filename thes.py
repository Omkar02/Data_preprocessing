import numpy as np
import cv2
import os

buff = 'buffer'
path = os.listdir(buff)
d = 0
i = 0
intensity = 1
kernel = np.ones((4,4),np.uint8)
kernal_erode = np.ones((6,6),np.uint8)
for file in path:
    path[i] = os.path.splitext(file)[0]
    text = path[i]
    text = text[:2]
    print('Name_char : ',text)
    i = i + 1
    original  = 'NEW/'+ text +'original_%d.jpg' % d
    threshold = 'NEW/'+ text +'Noise_%d.jpg' % d    # output directory
    d += 1
    img = cv2.imread(os.path.join(buff, file),0)
    noisy1 = img + img.std() * np.random.random(img.shape)
    alot = intensity * img.max() * np.random.random(img.shape)
    noisy2 = img + alot
    img1 = cv2.GaussianBlur(noisy2, (3, 3), 2)
    # erode = cv2.erode(img1, kernal_erode, iterations=6)

    ret, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
    erode = cv2.erode(th1, kernal_erode, iterations=2)
    dilation = cv2.dilate(erode, kernel, iterations=2)
    cv2.imwrite(original,img)
    cv2.imwrite(threshold, dilation)

print('Thresholding Done!')

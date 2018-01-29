
from scipy.misc import imsave
from scipy import misc
import numpy as np
import cv2
import os

Name_char = str('0')


folder = 'English(oLD)/Fnt/Sample001'
list = os.listdir(folder)                                                                   # dir is your directory path
number_files = len(list)

intensity = 2
d = 0
f = 0

print('***********************')
print('Nosinating...')
print('***********************')
for file in os.listdir(folder):
    outfile1 = 'buffer/'+ Name_char +'101_%d.jpg' % d
    outfile2 = 'buffer/' + Name_char + '202_%f.jpg' % f
    image = misc.imread(os.path.join(folder, file), mode="L")
    noisy1 = image + image.std() * np.random.random(image.shape)
    alot = intensity * image.max() * np.random.random(image.shape)
    noisy2 = image + alot
    imsave(outfile1, image)
    d = d + 1
    imsave(outfile2, noisy1)
    f = f + 1

print('Nosinating Done!')
print('***********************')
print('Starting Threshing')
print('***********************')
#*********************************************************
buff = 'buffer'
d = 0
for file in os.listdir(buff):
    threshold =  'data_new/'+ Name_char +'_%d.jpg' % d    # output directory
    d += 1
    img = cv2.imread(os.path.join(buff, file),0)
    img = cv2.medianBlur(img, 3)
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(threshold, th1)

print('Thresholding Done!')
print('***********************')
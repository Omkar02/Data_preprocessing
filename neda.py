from skimage.filters import threshold_mean
from scipy.misc import imsave
from scipy import ndimage
from scipy import misc
import numpy as np
import cv2
import os
#************************************************
i = str('0')
d = 0
a = 0
intensity = 2
myList_lable = []
#************************************************
while True:
     folder = 'Fnt/%a' %a
     print('Reading = ','|',folder,'Name = ',i)
     for file in os.listdir(folder):
          i = str(i)
          outfile1 = 'New/' + i + 's%d.jpg' % d
          image = misc.imread(os.path.join(folder, file), mode="L")
          # noisy1 = image + 3 * image.std() * np.random.random(image.shape)
          # alot = intensity * image.max() * np.random.random(image.shape)
          # noisy2 = image + alot
          imsave(outfile1, image)
          d = d + 1
     i = int(i)
     a = a + 1
     d = 0
     if i>=0 and i<=9:
          i = '0'+str(i)
     i = int(i)
     i = i + 1

     if a>=36:
          break
#************************************************
print('Done!')

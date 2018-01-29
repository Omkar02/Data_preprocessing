import numpy as np
import os
import pickle
from PIL import Image


#**************************************************************************
file_Name = "PICKEL/New.pkl"
img_data_list=[]
#**************************************************************************
data_path='New'
data_dir_list = os.listdir(data_path)
num_files = len(data_dir_list)
print(num_files)
d = 0
#**************************************************************************
for dataset in os.listdir(data_path):
    img = Image.open(os.path.join(data_path, dataset)).convert('L')
    img = img.resize((32, 32), Image.ANTIALIAS)
    img = np.reshape(img, (32, 32, 1))
    img_data_list.append(img)
    pe = ((num_files-d)/num_files)*100
    print('Data_Remaning = ',int(pe),'%' )
    d = d + 1

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255

data = (img_data)
print (img_data.shape)
fileObject = open(file_Name, 'wb')
pickle.dump(data, fileObject)


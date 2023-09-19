import os
import cv2
import glob
import shutil

import label_utils.csv_utils as csv_utils

path_imgs = 'objdet/data/MAS-TrainingImages2/sobel_imgs/'
csv_fname = 'objdet/data/MAS-TrainingImages2/sobel_imgs/labels.csv'
out_path = 'objdet/data/defect_imgs/'

if not os.path.exists(out_path):
    os.makedirs(out_path)

lists = glob.glob(path_imgs + '/*.png')

dt,_ = csv_utils.load_csv(csv_fname, path_imgs)
print(dt.keys())
for p in lists:
    fname = os.path.basename(p)
    if fname in dt:
        shutil.copy2(p, out_path +'/'+ fname)
        
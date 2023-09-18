import os
import numpy as np
import cv2
import glob


def norm(I,a,b):
    # return I in [a,b]
    return a + (b-a)*I


parentpath = 'C:\Program Files (x86)\Google\Cloud SDK\MAS-TrainingImages'
out_path = 'C:\Program Files (x86)\Google\Cloud SDK\MAS-TrainingImages2'

if not os.path.exists(out_path):
    os.mkdir(out_path)

for part in os.listdir(parentpath):
    part_path = os.path.join(parentpath, part)
    if not os.path.isdir(part_path):
        continue
    
    print(part)
    paths = glob.glob(os.path.join(part_path, '*.tiff'))
    for path in paths:
        im = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        fname = os.path.basename(path)
        fname,ext = os.path.splitext(fname)
        
        if fname.find('rgb') != -1 or fname.find('delta') != -1:
            continue
        
        # mask = im>0
        # foregound = im[mask]
        # lo,hi = foregound.min(), foregound.max()
        # print(lo,hi)
        # im[mask] = norm((foregound.astype(float)-lo)/(hi-lo), 1, 255)
        
        # lo,hi = im.min(), im.max()
        # print(lo,hi)
        
        # im = (im.astype(float)-lo)/(hi-lo)*255
        
        cv2.imwrite(os.path.join(out_path, f'{part}-'+fname+'.png'), im)

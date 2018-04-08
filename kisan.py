# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 00:56:20 2018

@author: Manoj
"""

import cv2
import numpy as np
import os
import imutils


path=os.path.dirname(os.path.abspath(__file__))+"\\"

imagepath = "images\\"
outpath = "outimages\\"


for infolder in os.listdir(path+imagepath):
    if os.path.isdir(path+imagepath+infolder):
        for infile in os.listdir(path+imagepath+infolder):
            print(path+imagepath+infolder+'\\'+infile)
            img_rgb = cv2.imread(path+imagepath+infolder+'\\'+infile)
            print(img_rgb.shape)
            res_img = cv2.resize(img_rgb,(400,250))
            cv2.imwrite(path+outpath+infolder+'\\'+infile.split('.')[0]+'_resize.jpg',res_img)
            rows,cols,_ = img_rgb.shape
            for angle in range(0,360,20):
                #rot = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
                #rot_img = cv2.warpAffine(res_img,rot,(cols,rows))
                rot_img = imutils.rotate_bound(res_img,angle)
                print(path+outpath+infolder+'\\'+infile.split('.')[0]+str(angle)+'.jpg')
                cv2.imwrite(path+outpath+infolder+'\\'+infile.split('.')[0]+str(angle)+'.jpg',rot_img)
        
        
    




import cv2
import os
import numpy as np


def display(f):
    img =cv2.imread(f.filename)
    path = '//Users//manasareddy//Desktop//programs//mini-project//static'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray =cv2.medianBlur(gray,5)
    edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(img,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray,(25,25),0)
    pencil=cv2.divide(gray,gray_blur,scale=250.0)
    
    cv2.imwrite(os.path.join(path,'img.jpg'),img)
    cv2.imwrite(os.path.join(path,'gray.jpg'),gray)
    cv2.imwrite(os.path.join(path,'edges.jpg'),edges)
    cv2.imwrite(os.path.join(path , 'color.jpg'),color)
    cv2.imwrite(os.path.join(path , 'cartoon.jpg'),cartoon)
    cv2.imwrite(os.path.join(path , 'gray_blur.jpg'),gray_blur)
    cv2.imwrite(os.path.join(path , 'pencil.jpg'),pencil)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


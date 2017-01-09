import numpy as np
import cv2
import sys

file1=sys.argv[1]
file2=sys.argv[2] 

img = cv2.imread(file1,0)
print "Starting CLAHE processing"

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite(file2,cl1)

print "Created file: {0}".format(file2)



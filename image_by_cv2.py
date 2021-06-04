import cv2
import numpy

# create the image and save the image in jpg format

img5 = numpy.zeros((500,500,3),numpy.uint8)
img5[0:250,0:250] = (255,125,0)
img5[0:250:,250:500] = (0,255,0)
img5[250:500,250:500] = (255,0,255)
img5[250:500:,0:250] = (0,0,255)

cv2.imshow('image',img5)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("created.jpg" , img5)

# -------swap the image-------
photo1 = cv2.imread('john.jpeg')
cp1 = photo1[0:180,0:250]
clr = cv2.cvtColor(cp1, cv2.COLOR_BGR2XYZ)
hs = numpy.hstack((cp1,clr))

cv2.imshow('image',hs)
cv2.waitKey(0)
cv2.destroyAllWindows()

temp = numpy.copy(hs)
temp[0:100,100:170] = hs[0:100,350:420]
temp[0:100,350:420] = hs[0:100,100:170]
cv2.imshow('image',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()

#------collage the image----------

roman = cv2.imread('roman.jpg')
rom = roman[:,100:600]
print(rom.shape)

cv2.imshow('image' , rom)
cv2.waitKey(0)
cv2.destroyAllWindows()


john = cv2.imread('john.jpeg')
john1 = john[0:180,0:250]

unkn = cv2.imread("unkn.jpeg")
unkn1 = unkn[0:180,0:250]

both = numpy.hstack((john1,unkn1))
print(both.shape)

collage = numpy.vstack((rom,both))

cv2.imshow('image',collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------collage end ------



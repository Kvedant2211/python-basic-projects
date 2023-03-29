#configurable objects
import cv2
source="car img.jpg" #we can convert img into any format
destination=input("Enter outut image name with format : ")
scale_p =int(input("Enter sacle percent amount of image : "))

src=cv2.imread(source,cv2.IMREAD_UNCHANGED) #for loading image
#cv2.show("title",src)

# Percent by which image is resized
#calculate scale_% of original img
nheight=int(src.shape[0]* scale_p /100)
nwidth=int(src.shape[1]* scale_p /100)


#resize image
op=cv2.resize(src,(nwidth,nheight))

cv2.imwrite(destination,op)
#cv2.waitKey(0)
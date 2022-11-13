import cv2 
import numpy as np 

class harris(object):  
    # loading image
    photo = cv2.imread('C:/Projects/hackaton/image/1.jpg')
    m = cv2.imread('C:/Projects/hackaton/image/1.png', 0)
    image = cv2.bitwise_and(photo, photo, mask=m)
    image.shape
    w = image.shape[1]
    h = image.shape[0]
    if h>w:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    # convert the input image into grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    # convert the data type 
    img_gray = np.float32(img_gray) 
    
    # implementing cv2.cornerHarris method 
    hcd_img = cv2.cornerHarris(img_gray, 5, 5, 0.08)
    orb = cv2.ORB_create(300)
    keypoint, des = orb.detectAndCompute(image, None)
    # marking dilated corners 
    hcd_img = cv2.dilate(hcd_img, None) 
    
    # reverting back to the original image
    image[hcd_img > 0.01 * hcd_img.max()]=[0, 97, 38] 
    
    # show the image
    """cv2.imshow('Image with corners', image) 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)"""
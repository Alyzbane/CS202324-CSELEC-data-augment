import cv2
import numpy as np

def segmentation(image):
    # Convert the image to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Apply segmentation (example: thresholding) 
    _, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    
    return segmented_image
    
    
def cannyedge(image):
    """
    Return the canny edge using the auto feature
    Measure the low and high and tolerance that lines would
    show in the image

    Parameters
    ----------
    image : TYPE
        DESCRIPTION.

    Returns
    -------
    auto_canny : TYPE
        DESCRIPTION.

    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Tolerance value for lines
    sigma = 0.3 
    median = np.median(image) 
    
    
    # Automatic canny edge detection using computed median
    # 30% low in this case
    lower = int(max(0, (1.0 - sigma) * median))
    
    # Lower the the threshold sigma % lower than median
    # if the value is below 0 then take 0 as the value

    upper = int(min(255, (1.0 + sigma) * median))
    auto_canny = cv2.Canny(image, lower, upper)
    
    # cv2.imshow("AutoCanny", auto_canny)
    # cv2.waitKey(0)
    # cv2.destroyWindow()
    return auto_canny

def grayscale(image):
    """
    Will write an grayscale image in the specified path

    Parameters
    ----------
    image : Numpy.array
        A valid image file
    path : String
        Path of file

    Returns
    -------
    None.

    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if __name__ == "__main__":
    pass
      
# Future preprocess refined for image lines extraction
def convolution2d(image):
    """  
    
    Laplacian of Gaussian (LoG) kernel
    
    Parameters
    ----------
    image : Numpy array
        A valid image

    Returns
    -------
    out : Numpy array
        The result of filtering the image using the Laplacian of Gaussian
        (LoG) kernel

    """
    

    kernel = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])
    out = cv2.filter2D(image, ddepth=-1, kernel=kernel)
    out = cv2.convertScaleAbs(out)
    
    return out


    
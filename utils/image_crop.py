import cv2
import numpy as np
import glob
import os
from tqdm import tqdm

def process_one(path, y_small, y_large, x_small, x_large):
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    #print(img.shape) # Print image shape
    #cv2.imshow("original", img)
    
    # Cropping an image
    cropped_image = img[y_small:y_large, x_small:x_large]
    
    # Display cropped image
    #cv2.imshow("cropped", cropped_image)
    basepath = os.path.dirname(path) + "\\crop_" + os.path.basename(path)
    is_success, im_buf_arr = cv2.imencode(".jpg", cropped_image)
    im_buf_arr.tofile(basepath)

    #Save the cropped image
    cv2.imwrite(basepath, cropped_image)


def process_folder(path):

    ## use glob regex to find all the image in a folder
    all_image = glob.glob(path)

    #print(os.path.dirname(all_image[0]))
    for i, path_item in tqdm(enumerate(all_image)):
        
        process_one(path_item)

## change the path and the two diagnal points pixel value
process_one(path = './asset/front.png', y_small=416, y_large=1195, x_small=1046, x_large=1910)

#process_folder(r"D:\NLP\语料\语料\G2-B-a\**\**\*.png")

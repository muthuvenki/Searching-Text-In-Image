#Author : Venkat Chidambaram
#Last Date of udpate: 20 Mar 2020
#Input: Any Image file & Keyword to search
#Output: Highlight the keyowrd in the same img

# Importting the neccessary Lib
# Important lib & imports
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import glob
from pytesseract import Output
import cv2

# GLobal Folder Location
FolderLocation = "ocr/" 
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 

# Convert tiff img to jpeg # Use the function if its needed
def conver_tif_jpg(name):
    im = Image.open(FolderLocation + name)
    name = str(name).rstrip(".tif")
    im.save(FolderLocation + name + '.jpg', 'JPEG')
    return name + '.jpg'

# Preprocessing text : lower, removing special case, spellchecker
def text_clean(text):
    text = text.lower()
    text = text.replace(",","")
    return text

# Funtion Which do all the execution steps
def find_keyword_higlight(TestFileName , singlekey):
    img = cv2.imread(FolderLocation + TestFileName)
    d = pytesseract.image_to_data(img, output_type=Output.DICT, lang='eng', config=pytesseract.pytesseract.tesseract_cmd )
    n_boxes = len(d['level'])

    overlay = img.copy()

    # For roll back when next occurance word not found
    original_img = img.copy()

    for i in range(n_boxes):
        Flag = True
        if text_clean(d['text'][i]) == text_clean(singlekey[0]):

            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            (x1, y1, w1, h1) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(overlay, (x, y), (x1 + w1, y1 + h1), (255, 0, 0), -1)

            alpha = 0.4  # Transparency factor.
            # Following line overlays transparent rectangle over the image
            img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

            r = 1000.0 / img_new.shape[1]  # resizing image without loosing aspect ratio
            dim = (1000, int(img_new.shape[0] * r))

            # perform the actual resizing of the image and show it
            resized = cv2.resize(img_new, dim, interpolation=cv2.INTER_AREA)

            for counter in range(1,len(singlekey)):
                #print(counter)
                if text_clean(d['text'][i+counter]) == text_clean(singlekey[counter]):
                    #print(d['text'][i+counter])

                    (x, y, w, h) = (d['left'][i+counter], d['top'][i+counter], d['width'][i+counter], d['height'][i+counter])
                    (x1, y1, w1, h1) = (d['left'][i+counter], d['top'][i+counter], d['width'][i+counter], d['height'][i+counter])
                    cv2.rectangle(overlay, (x, y), (x1 + w1, y1 + h1), (255, 0, 0), -1)

                    alpha = 0.4  # Transparency factor.
                    # Following line overlays transparent rectangle over the image
                    img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

                    r = 1000.0 / img_new.shape[1]  # resizing image without loosing aspect ratio
                    dim = (1000, int(img_new.shape[0] * r))

                    # perform the actual resizing of the image and show it
                    resized = cv2.resize(img_new, dim, interpolation=cv2.INTER_AREA)

                    # For rollback
                    Flag = False

            #print(Flag)
            if Flag:
                # Rolling back since no next occurance word is found
                overlay = original_img.copy()

    #cv2.imshow('img', resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.imwrite(FolderLocation + TestFileName ,resized)
    return TestFileName

# Load the same img for keyword search
TestFileName = 'A9426720-Again-2514103_8.tif'
# Convert tif to jpeg 
#TestFileName = conver_tif_jpg(TestFileName) # Use if needed

# Mention the keyword 
keywords = ['for a medication']

# Main Function 
for singlekey in keywords:
    #print(singlekey)
    singlekey = singlekey.split(' ')
    print(singlekey)
    
    find_keyword_higlight(TestFileName,singlekey)
    
    #break # Break for keywords
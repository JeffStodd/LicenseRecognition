import pytesseract
import cv2
from PIL import Image

def main():
    

def preProcess(img):
    
    pass

def detect(img):

    #run detection
    data = pytesseract.image_to_data(img) #~2.5fps
    

    #split string into array of strings
    rows = data.splitlines()

    #skip title row
    for i in range(1, len(rows)):
        #convert string to array based on \t delimiter
        r = rows[i].split('	')
        
        #check if row is proper length, and text is not an empty string
        #only show detections with confidence >= 80
        if len(r) == 12 and not (r[11] == ' ' or r[11] == '') and int(r[10]) >= 80:
            #draws green rectangle with thickness 2 on image at x,y to x+w, y + h
            cv2.rectangle(front, (int(r[6]), int(r[7])), (int(r[6]) + int(r[8]), int(r[7]) + int(r[9])), (0, 255, 0), 2)
            print(r[11])
    
    cv2.imshow("Preview", front)
    cv2.imwrite("result.jpg", front)
    
main()


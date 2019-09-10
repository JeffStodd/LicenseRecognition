import pytesseract
import cv2
from PIL import Image

def main():

    #load img
    front = cv2.imread("022.jpg")

    #run detection
    #plate = pytesseract.image_to_string(front)
    #boxes = pytesseract.image_to_boxes(front)
    data = pytesseract.image_to_data(front) #~2.5fps
    

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

    print(data)
    cv2.imshow("Preview", front)
    cv2.imwrite("result.jpg", front)

    
main()


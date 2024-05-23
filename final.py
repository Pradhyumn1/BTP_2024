import cv2
import pytesseract
import easyocr
import os

# Load the Haar cascade classifier
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

# Initialize the OCR readers
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # If necessary
reader = easyocr.Reader(['en'], gpu=False) 

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
            img_roi = img[y: y + h, x: x + w]

            # OCR using both Pytesseract and easyocr
            text_pytesseract = pytesseract.image_to_string(img_roi)
            cleaned_text = ''.join(e for e in text_pytesseract if e.isalnum())  

            output_easyocr = reader.readtext(img_roi) 
            if output_easyocr:
                text_easyocr = output_easyocr[-1][1]
                confidence = output_easyocr[-1][2] 

                # Print results (you can choose which OCR output to display)
                print("Pytesseract:", cleaned_text) 
                print("EasyOCR:", text_easyocr, "(Confidence:", confidence, ")")

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

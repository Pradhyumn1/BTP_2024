import cv2
import pytesseract
import matplotlib.pyplot as plt
import easyocr
from IPython.display import Image
import os


# Load the Haar cascade classifier
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

reader = easyocr.Reader(['en'], gpu=False, recognizer=False) 

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
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)

        # OCR using Pytesseract
        text = pytesseract.image_to_string(img_roi)
        cleaned_text = ''.join(e for e in text if e.isalnum())
        print("Extracted Number:", cleaned_text)

        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

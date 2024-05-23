import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
import os

# Load the Haar cascade classifier
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False) 

# Process images from the 'plates' folder
for filename in os.listdir("plates"):  
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filepath = os.path.join("plates", filename)

        img = cv2.imread(filepath)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in plates:
            img_roi = img[y: y + h, x: x + w]

            output = reader.readtext(img_roi) 

            if output:
                text = output[-1][1]  # Get the recognized text
                confidence = output[-1][2]  # Get the confidence score

                if confidence > 0.5:  # Optional confidence thresholding
                    print("Extracted Text:", text)
                    print("Confidence Score:", confidence)

                # Visualization (optional)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# ... (Optional image display and cleanup code) ...

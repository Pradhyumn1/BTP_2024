# Car-Number-Plates-Detection

Automatic License Plate Recognition (ALPR) System

This project uses OpenCV, Pytesseract, and EasyOCR to detect and extract license plate information from live video or images.

Features:

* Real-time license plate detection from video streams.
* Uses Haar cascade classifier for plate detection.
* OCR with Pytesseract and EasyOCR for text extraction.
* Combines both OCR engines for better accuracy.
* Provides confidence scores for EasyOCR results.
* Written in Python for easy customization.

Requirements:

* Python 3.x
* OpenCV (cv2)
* Pytesseract (pytesseract)
* EasyOCR (easyocr)
* Haar cascade classifier file (e.g., haarcascade_russian_plate_number.xml)
* Webcam or video file

Installation:

1. Clone the repository:
   git clone https://github.com/your-username/your-repository.git
2. Install dependencies:
   pip install -r requirements.txt 
   (Create requirements.txt and list the libraries.)
3. (Optional) Download Tesseract OCR:
   https://github.com/UB-Mannheim/tesseract/wiki
   Add Tesseract to your system PATH or set the pytesseract.pytesseract.tesseract_cmd variable.
4. (Optional) Get a suitable Haar cascade classifier for your plate format.

Usage:

1. Run the script:
   python alpr.py
   (Replace alpr.py with your script's name.)
2. The script will open a video stream or use a video file.
3. Detected plate numbers will be printed to the console.
4. Press 'q' to quit.

Configuration:

* Adjust "min_area" in the code to control the minimum size of detected plates.
* Replace "haarcascade_russian_plate_number.xml" with a different classifier for other plate formats.

Acknowledgments:

* Haar cascade classifier: https://github.com/opencv/opencv/tree/master/data/haarcascades
* Pytesseract: https://github.com/madmaze/pytesseract
* EasyOCR: https://github.com/JaidedAI/EasyOCR

Contributions welcome!

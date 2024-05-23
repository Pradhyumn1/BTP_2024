import csv
import re
import logging

logging.basicConfig(filename='ocr_processing.log', level=logging.INFO)

def process_ocr_line(line):
    """Extracts OCR engine, result, and confidence from an OCR output line.
    Handles lines with invalid format.
    """
    parts = re.split(r'\s+', line.strip())
    if len(parts) >= 3:
        engine = parts[0].rstrip(':')
        result = parts[1]
        confidence = float(parts[3].lstrip('(').rstrip(')'))
        return engine, result, confidence
    else:
        logging.warning(f"Invalid OCR line format: {line}")
        return None, None, None

def generate_csv(ocr_data_file, output_csv_file):
    """Processes OCR data, associates it with images, and saves as CSV."""
    with open(ocr_data_file, 'r') as f:
        ocr_data = f.readlines()

    results = []
    image_index = 1
    header_skipped = False
    for line in ocr_data:
        if line.strip():
            if not header_skipped:
                header_skipped = True  # Skip the header line
                continue

            engine, result, confidence = process_ocr_line(line)
            if confidence is not None and confidence >= 0.3: 
                image_name = f"image{image_index}.jpg"
                results.append([image_name, engine, result, confidence])
                image_index += 1

    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image_name', 'ocr_engine', 'ocr_result', 'confidence'])
        writer.writerows(results)

# Modify paths as needed
ocr_data_file = 'ocr_data.txt'
output_csv_file = 'ocr_results.csv'

generate_csv(ocr_data_file, output_csv_file)

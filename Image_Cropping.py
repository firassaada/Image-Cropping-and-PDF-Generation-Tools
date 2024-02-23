import cv2
import numpy as np

def crop_document(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply edge detection
    margin_size=10
    edges = cv2.Canny(gray, 100, 250)
    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Select the largest contour (assuming it's the document)
    contour = max(contours, key=cv2.contourArea)
    # Approximate the contour to a polygon
    epsilon = 0.05 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    # Ensure approx has exactly four points
    if len(approx) != 4:
        raise ValueError("Unable to find four corners of the document,Please retake the photo")
    # Determine the four corners of the document
    corners = np.float32(approx.reshape(4, 2))
    # Order the corners clockwise
    rect = np.zeros((4, 2), dtype="float32")
    s = corners.sum(axis=1)
    rect[0] = corners[np.argmin(s)]
    rect[2] = corners[np.argmax(s)]
    diff = np.diff(corners, axis=1)
    rect[1] = corners[np.argmin(diff)]
    rect[3] = corners[np.argmax(diff)]
    # Perform perspective transformation
    width = max(np.linalg.norm(rect[0] - rect[1]), np.linalg.norm(rect[2] - rect[3]))
    height = max(np.linalg.norm(rect[1] - rect[2]), np.linalg.norm(rect[3] - rect[0]))
    dst = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (int(width), int(height)))
    # Crop the transformed image
    cropped_image = warped[0:int(height), 0:int(width)]
   # margin_image = cv2.copyMakeBorder(warped, 25, 25, 25,25, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    # Apply edge detection
    return cropped_image






























































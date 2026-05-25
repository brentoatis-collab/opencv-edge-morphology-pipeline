import cv2
import numpy as np

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Verify webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit the application.")

while True:

    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)

    # Create kernel for morphological operations
    kernel = np.ones((3, 3), np.uint8)

    # Apply dilation to strengthen edges
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # Apply erosion to remove noise
    eroded = cv2.erode(dilated, kernel, iterations=1)

    # Display original frame
    cv2.imshow('Original Frame', frame)

    # Display grayscale frame
    cv2.imshow('Grayscale Frame', gray)

    # Display edge detection frame
    cv2.imshow('Canny Edge Detection', edges)

    # Display dilation result
    cv2.imshow('Dilated Edges', dilated)

    # Display erosion result
    cv2.imshow('Eroded Edges', eroded)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
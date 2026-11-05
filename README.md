> **Applied AI portfolio project by Brent Oatis, MBA**
> Applying edge detection and morphology to inspection, defect, and image-cleanup workflows.

# CST544_Week2_EdgeDetection

# Real-Time Edge Detection and Morphological Filtering

## Project Overview

This project demonstrates a real-time computer vision pipeline using Python and OpenCV. The application captures live webcam video, preprocesses image frames, detects object boundaries using the Canny Edge Detection algorithm, and refines edge structures using morphological operations such as dilation and erosion.

The purpose of this assignment was to explore foundational computer vision preprocessing techniques and understand how edge refinement improves downstream artificial intelligence and image analysis systems.

---

# Technologies Used

- Python 3
- OpenCV
- NumPy
- VS Code
- GitHub

---

# Features

- Real-time webcam video capture
- Grayscale image preprocessing
- Gaussian blur noise reduction
- Canny edge detection
- Morphological filtering using dilation and erosion
- Real-time OpenCV visualization windows
- Structured project organization for reproducibility

---

# Computer Vision Workflow

The application follows the workflow below:

1. Capture live webcam frame
2. Convert frame to grayscale
3. Apply Gaussian blur to reduce image noise
4. Perform Canny edge detection
5. Apply dilation to strengthen edge structures
6. Apply erosion to reduce excess noise
7. Display processed frames in real time

---

# Morphological Operations

## Dilation

Dilation strengthens detected edge boundaries by expanding contour pixels. This operation reconnects broken edges and improves contour continuity.

## Erosion

Erosion removes excess edge noise and refines the final image structure by shrinking unnecessary pixel expansions created during dilation.

Together, these operations improve image clarity and edge precision within computer vision systems.

---

# Real-World Applications

These computer vision techniques are commonly used in:

- Robotics and autonomous navigation
- Industrial inspection and quality control
- Medical imaging systems
- Security and surveillance systems
- Object recognition and tracking
- AI-powered vision analysis

---

# Project Structure

```plaintext
CST544_Week2_EdgeDetection/
│
├── edge_detection.py
├── README.md
├── requirements.txt
├── screenshots/
│   ├── original_frame.png
│   ├── grayscale_frame.png
│   ├── canny_edges.png
│   ├── dilated_edges.png
│   ├── eroded_edges.png
│   ├── terminal_execution.png
│   └── project_structure.png
│
└── presentation/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/brentoatis-collab/opencv-edge-morphology-pipeline.git
```

---

# Create Virtual Environment

## Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Mac/Linux

```bash
python3 edge_detection.py
```

## Windows

```bash
python edge_detection.py
```

---

# Expected Output

The application displays:

- Original webcam feed
- Grayscale preprocessing frame
- Canny edge detection output
- Dilated edge output
- Eroded edge output

Press:

```plaintext
q
```

to exit the application.

---

# Example Processing Pipeline

## Original Video Feed
Live webcam frame captured using OpenCV.

## Grayscale Conversion
Reduces computational complexity while preserving image structure.

## Canny Edge Detection
Identifies rapid intensity transitions and extracts object contours.

## Morphological Filtering
Refines edge structures and improves contour clarity.

---

# Learning Outcomes

This project reinforced:

- Real-time OpenCV implementation
- Computer vision preprocessing techniques
- Edge detection fundamentals
- Morphological image filtering
- Real-time frame rendering
- Image analysis workflow design
- Debugging and AI vision system development

---

# References

Bradski, G. (2000). *The OpenCV library*. *Dr. Dobb’s Journal of Software Tools*.

OpenCV. (2026). *OpenCV documentation*. https://opencv.org/

Szeliski, R. (2022). *Computer vision: Algorithms and applications* (2nd ed.). Springer. https://szeliski.org/Book/

---

# Video Source

Live webcam video feed captured using OpenCV.

---

# Author

Brent Oatis  
CST 544 – Artificial Intelligence in Computer Vision  
Concordia University St. Paul

---

# Final Reflection

This project demonstrated how preprocessing quality directly impacts downstream computer vision performance. Through grayscale conversion, edge detection, and morphological filtering, the application transformed raw visual input into refined structural data suitable for modern AI-driven systems.

The assignment also provided practical experience working with OpenCV pipelines, real-time webcam processing, and computer vision workflow implementation.

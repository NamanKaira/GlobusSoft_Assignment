# Drone Detection API

## Overview

This project is a simple FastAPI service that detects drones from a single sky image.

A lightweight YOLOv8 Nano model is used for object detection. The API accepts an image, performs detection, and returns:

- Bounding boxes
- Confidence scores
- Total number of detected drones

---

## Features

- Upload a single image
- Detect drones using YOLOv8 Nano
- Return bounding box coordinates
- Return confidence scores
- Return total drone count
- FastAPI-based REST API
- Single-image inference

---

## Project Structure

```text
drone-detection-api/
│
├── app.py
├── detector.py
├── requirements.txt
├── README.md
├── uploads/
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd drone-detection-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /detect

Upload a single image and receive drone detection results.

### Supported Formats

- JPG
- JPEG
- PNG

---

## Example Response

```json
{
  "count": 1,
  "detections": [
    {
      "bbox": [63, 25, 606, 477],
      "confidence": 0.70
    }
  ]
}
```

---

## Response Fields

| Field | Description |
|---------|------------|
| count | Total number of detected drones |
| detections | List of detected objects |
| bbox | Bounding box coordinates in the format [x1, y1, x2, y2] |
| confidence | Detection confidence score |

---

## Testing

The API was tested with:

- Image containing a drone/aircraft
- Image containing multiple drones/aircraft
- Empty sky image

Example response for an empty sky image:

```json
{
  "count": 0,
  "detections": []
}
```

---

## Technical Details

- Framework: FastAPI
- Detection Model: YOLOv8 Nano
- Image Processing: OpenCV
- Inference Type: Single Image Inference

---

## Note

YOLOv8 Nano is used as a lightweight object detection model.

The default COCO dataset used by YOLOv8 does not contain a dedicated drone class. Therefore, the **airplane** class is used as a proxy for drone detection in this implementation.

The API still provides:

- Bounding boxes
- Confidence scores
- Total detected count

This project is intended as a simple demonstration of image-based drone counting using FastAPI and YOLO.

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Ultralytics
- OpenCV
- NumPy

---

## Author

Drone Detection API built using FastAPI and YOLOv8 Nano.

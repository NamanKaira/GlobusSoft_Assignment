from ultralytics import YOLO

# Load lightweight YOLO model
model = YOLO("yolov8n.pt")


def detect_drones(image_path):
    """
    Detect drones in image.

    Returns:
    {
        "count": int,
        "detections": [
            {
                "bbox": [x1,y1,x2,y2],
                "confidence": 0.91
            }
        ]
    }
    """

    results = model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            class_name = model.names[class_id]

            # Filter only drone-like classes
            # COCO does not have drone class,
            # so for demo we can use airplane.
            if class_name == "airplane" and confidence > 0.5:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "confidence": round(confidence, 3)
                })

    return {
        "count": len(detections),
        "detections": detections
    }

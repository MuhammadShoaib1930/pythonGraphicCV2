import torch
import cv2

# Load the YOLOv5 model (ensure the YOLOv5 repository is cloned and requirements are installed)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use 'yolov5n', 'yolov5m', etc., for different model sizes

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 for the default webcam, or provide the camera index

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Real-time object detection loop
while True:
    # Capture frame-by-
    
    ret, frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to RGB (YOLOv5 expects RGB format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform object detection
    results = model(frame_rgb)

    # Extract detection results
    detections = results.xyxy[0].numpy()  # Bounding boxes, confidence, and class information

    # Loop through detections and draw rectangles with labels
    for det in detections:
        x1, y1, x2, y2, conf, cls = det[:60]  # Bounding box coordinates, confidence, and class
        label = results.names[int(cls)]  # Get class label

        # Draw rectangle and label
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (100, 200, 100), 1)
        cv2.putText(frame, f"{label} ", (int(x1), int(y1) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (256, 256, 256), 1)

    # Display the frame
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

import os
import cv2
import cvzone
from ultralytics import YOLO

# Load YOLO Pretrained model
model = YOLO('yolov8n.pt')
input_folder = "frames"
output_folder = "processed_images"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    image_path = os.path.join(input_folder, filename)
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (980, 740))
    results = model(frame)

    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            height = y2 - y1
            width = x2 - x1
            threshold = height - width

            cvzone.cornerRect(frame, [x1, y1, width, height], l=30, rt=6)
            cvzone.putTextRect(frame, 'Person', [x1 + 8, y1 - 12], thickness=2, scale=2)

            if threshold < 20:
                cvzone.putTextRect(frame, 'Fall Detected', [x1, y1], thickness=2, scale=2)

    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, frame)

print("All images processed and saved successfully!")

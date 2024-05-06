from ultralytics import YOLO

# Load YOLO model
model = YOLO()
model.train(data='dataset/data.yaml',epochs = 50)
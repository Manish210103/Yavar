from ultralytics import YOLO

model = YOLO("best.pt")
model.val(data = 'dataset/data.yaml')

from ultralytics import YOLO
import sys

if len(sys.argv) < 2:
    sys.exit("Model data path missing")

# Load a model
model = YOLO('yolov8m.pt')  # pretrained model

# Train the model
model.train(data=sys.argv[1], epochs=100, imgsz=640)
from ultralytics import YOLO
import sys

if len(sys.argv) < 2:
    sys.exit("Model data path missing")

# Load a model
model = YOLO(sys.argv[1])  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
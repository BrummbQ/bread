from ultralytics import YOLO
import sys

if len(sys.argv) < 3:
    sys.exit("Model or source data path missing")

# Load a model
model = YOLO(sys.argv[1])  # load a custom model

# run predict
model.predict(sys.argv[2], save=True, show=True, hide_labels=False, conf=0.1)
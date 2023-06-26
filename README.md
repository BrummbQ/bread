# Bread bubble model

Bubble model training and detection

## Setup

You need python3 and the yolo library, see https://docs.ultralytics.com/quickstart/

## Training

Train a new model with:

```
python3 train_bubbles.py <path_to_data.yml>
```

And for validation:

```
python3 val_bubbles.py <path_to_trained_model>
```

## Detection

Lets detect some bubbles:

```
python3 predict_bubbles.py <path_to_trained_model> <path_to_jpeg>
```

# Bubble blob detector

Blob detection with opencv

## Setup

Install python 3 and dependencies:

```
# create venv
python -m venv env

# activate
source env/bin/activate

# install deps
pip install -r requirements.txt
```

## Run detector

```
# test image with bubbles
python blob_detector.py --image data/testimg/bubbles.jpg

# image without bubbles
python blob_detector.py --image data/testimg/no_bubbles.jpg
```

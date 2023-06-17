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

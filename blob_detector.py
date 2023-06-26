# Standard imports
import cv2
import argparse
import os
import numpy as np;
 
parser = argparse.ArgumentParser(description='Template matcher')
parser.add_argument('--image', type=str, action='store',
                    help='The image to be used as template')
parser.add_argument('--show', action='store_true',
                    help='Shows result image')
parser.add_argument('--save-dir', type=str, default='./',
                    help='Directory in which you desire to save the result image')

args = parser.parse_args()

# Read image
im = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 250
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.57
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.35

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)
print("Matches:", len(keypoints))

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imwrite(os.path.join(args.save_dir, 'output.jpg'), im_with_keypoints)
if args.show:
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)
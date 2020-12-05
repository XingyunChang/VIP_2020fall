import os
import glob
import random
import numpy as np
import matplotlib.pyplot as plt

from imageio import imread, imsave, mimsave
from IPython.display import Image

# setup the video dataset
ROOT = "Dataset/"
ACTIONS = ["botharms", "crouch", "leftarmup", "punch", "rightkick"]

# select a random sequence for a random action
action = random.choice(ACTIONS)
folders = glob.glob(os.path.join(ROOT, action, "*"))
folder = random.choice(folders)

# get the sorted image files
files = sorted(glob.glob(os.path.join(folder, "*.pgm")))

# get the images 
images = [np.array(imread(path)) for path in files]

print(f"Sequence: {folder}")
print(f"Sequence contains {len(files)} images")

# view all of the images in the squence
h = 10
w = len(images) // h + 1
fig, axs = plt.subplots(w, h, figsize=(2 * h, 2 * w))
for ax in axs.flat:
    ax.axis("off")
for img, ax in zip(images, axs.flat):
    ax.imshow(img)

# This method substract the background of the sequence of image
# It only keeps the pixels that are greater than the threshold input
def subtract_bg(image, threshold):
    foreground_image = image.copy()
    # if it's greater than threshold -> background
    bg = foreground_image > threshold 
    # set background as 0
    foreground_image[bg] = 0
    return foreground_image

# This method compare the difference between two consecutive frames
# It keeps the difference if the difference is greater than the threshold
# This threshold is the "difference threshold"
def diff_between_frames(image1, image2, threshold):
    diff = np.zeros_like(image1, dtype="bool")
    temp = np.abs(image1 - image2) > threshold
    diff[temp] = True
    return diff

# First, we use a subtract_bg method to remove background, only keeping the pixels that are greater than the background threshold.
# Second, we use a diff_between_frames method to calculate the binary foreground difference between two images.
# Third, we calculate the motion history image value. 
def compute_motion_history_image(images, background_subtraction_threshold, difference_threshold):
    assert len(images) > 0
    MHI = np.zeros_like(images[0])
    subtracted_res = subtract_bg(images[0], background_subtraction_threshold)
    for img in images[1:]:
        curr_subtracted_res = subtract_bg(img, background_subtraction_threshold)
        image_diff = diff_between_frames(subtracted_res, curr_subtracted_res, difference_threshold)
        MHI = MHI - 1
        length = len(images)
        MHI[image_diff] = length - 1
        MHI[MHI < 0] = 0
        subtracted_res = curr_subtracted_res
        res = MHI / np.max(MHI)
    return res

# display the extracted images 
getMHIs = []
getLabels = []
fig, axs = plt.subplots(5, 4, figsize = (15,15))
for i, action in enumerate(ACTIONS):
    files = glob.glob(os.path.join(ROOT, action, "*"))
    for j, folder in enumerate(files):
        sources = glob.glob(os.path.join(folder, "*.pgm"))
        images = []
        for f in sources:
            images.append(np.array(imread(f)))
        MHI = compute_motion_history_image(images, background_subtraction_threshold=38000, difference_threshold=5500)
        # get h, w and apply to MHI
        height, width = MHI.shape
        getMHIs.append(MHI.reshape((height, width, 1)))
        getLabels.append(action)
        axs[i][j].imshow(MHI, cmap = "jet")
plt.show()
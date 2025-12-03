import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def annotate(impath, n_points=-1):  # Changed default to -1 for unlimited
    im = np.array(Image.open(impath))

    plt.imshow(im)
    # Clear instructions for the user
    plt.title("Left click: Add Point | Right click: Remove Last | Enter: Save & Exit")

    print(f"Annotating {impath}...")
    print("Press 'Enter' or 'Middle Click' to finish collecting points.")

    # n=-1 means unlimited clicks until 'Enter' is pressed
    # mouse_add=1 (Left Click), mouse_pop=3 (Right Click), mouse_stop=2 (Middle Click)
    clicks = plt.ginput(n=n_points, timeout=0, show_clicks=True)

    plt.close()

    print(f"Collected {len(clicks)} points")
    return np.array(clicks)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <image_path> <output_path.npy>")
    else:
        points = annotate(sys.argv[1])
        np.save(sys.argv[2], points)
        print(f"Saved to {sys.argv[2]}")

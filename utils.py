import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

def load_image(img_path):
    return cv2.imread(img_path)


def show_images(imgs, titles):
    assert len(imgs) == len(titles)

    plt.figure(figsize=(15, 5))

    sub_plots_num = len(imgs)

    for i in range(sub_plots_num):
        plt.subplot(100 + 10 * sub_plots_num + i + 1)
        plt.imshow(cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()


def to_homo(p):
    return np.array([p[0], p[1], 1])
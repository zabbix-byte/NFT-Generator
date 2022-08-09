from app.components import Components


# libs
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import random


class BaseImage(Components):
    def __init__(self, n:int, image: np.array, components_types: list, complements: list, backgrounds: list) -> None:
        super().__init__(complements ,components_types)

        self._n = n
        self._image = image

        # returns the w and h in px
        self._width, self._height = self._image.shape[:2]

        # This is use to plt base image
        plt.imshow(img.imread(random.choice(backgrounds)))
        plt.imshow(self._image)

    def save(self) -> None:
        plt.gca().set_axis_off()
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.savefig(f'./nft_generated/{self._n}.png', bbox_inches='tight', pad_inches = 0)
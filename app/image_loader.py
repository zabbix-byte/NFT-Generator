
from app.baseimage import BaseImage

# libs
import matplotlib.image as img
import matplotlib.pyplot as plt
import random


class ImageLoader(BaseImage):
    def __init__(self, n:int, base_image: str, components_types: list, complements: list, backgrounds: list) -> None:
         super().__init__(n, img.imread(base_image), components_types, complements, backgrounds)
    
    def put_components_in_position(self):
        data_groups = {}

        ## Grouping the data
        for i in self.types_com:
            data_groups[i] =  []
            for f, t in zip(self.com_files, self.com_type):
                if t == i:
                    data_groups[i].append(f)
        
        for i in data_groups:
            comp_to_show = random.choice(data_groups[i])
            if comp_to_show is not None:
                plt.imshow(comp_to_show)

        


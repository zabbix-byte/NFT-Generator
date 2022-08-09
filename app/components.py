import matplotlib.image as img


class Components:
    com_files = []
    com_size = []
    com_type = []

    def __init__(self, components: list, components_types: list) -> None:
        self.types_com = components_types

        # This is to randomise no dress
        for i in self.types_com:
            self.com_files.append(None)
            self.com_size.append(None)
            self.com_type.append(i)

        for i in components:
            if i['type'] not in self.types_com:
                print('You are putting a component type that you have not declared')
                exit()

            self.com_type.append(i['type'])
            c_img = img.imread(i['file'])
            self.com_files.append(c_img)
            width, height = c_img.shape[:2]
            self.com_size.append({'w': width, 'h': height})


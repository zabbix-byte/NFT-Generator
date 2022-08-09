from email.mime import base
import tkinter as tk
from tkinter import filedialog as fd
from ttkthemes import ThemedTk
from PIL import ImageTk, Image  

class BaseUI(ThemedTk):
    def __init__(self) -> None:
        super().__init__()
        self.font_family = 'Inter'
        self.app_windows_x = 1280
        self.app_window_y = 720
        self.theme = 'yaru'

        ### APP PARAMS
        self.base_file = None

        self.title('NFT Generator Alpha')
        self.configure(background='white',)

        self.geometry(f'{self.app_windows_x}x{self.app_window_y}')
        self.minsize(self.app_windows_x, self.app_window_y)
        self.maxsize(self.app_windows_x, self.app_window_y)

        barra_menus = tk.Menu()
        barra_menus.configure(background='white', borderwidth=0)
        barra_menus.add_separator()

        menu_list = [{'ADD BASE TEMPLATE': self.add_base_file}, {'ADD BACKGROUNDS': None},
                     {'ADD COMPONENT TYPES': None}, {'ADD COMPONENTS': None}]

        for i in range(len(menu_list)):
            for j in menu_list[i]:
                barra_menus.add_command(label=j,
                                        command=menu_list[i][j],
                                        background='#189AA7',
                                        foreground='#F9ECE4',
                                        activebackground='white',
                                        activeforeground='#189AA7',
                                        
                                        )

        self.config(menu=barra_menus)

        self.base_file_frame()



    def base_file_frame(self):
        pass

    def add_base_file(self):
        filetypes = (
            ('png', '*.png'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        self.base_file = filename

        basewidth = 300

        image1 = Image.open(filename)
        wpercent = (basewidth / float(image1.size[0]))
        hsize = int((float(image1.size[1]) * float(wpercent)))
        img = image1.resize((basewidth, hsize), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)
        label1 = tk.Label(image=test)
        label1.image = test
        label1.place(relx = 0.05,
                  rely = 0.4,
                  anchor ='w')

app = BaseUI()
app.mainloop()

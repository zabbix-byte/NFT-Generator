import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import json
from tkinter import messagebox

file_name_config = './config_app.json'
file_config_e = open(file_name_config, 'r')
file_config = json.load(file_config_e)
file_config_e.close()


class BaseUI(ThemedTk):
    def __init__(self) -> None:
        super().__init__()
        self.font_family = ('Inter', 11)
        self.app_windows_x = 1280
        self.app_window_y = 720
        self.theme = 'yaru'

        self.title('NFT Generator Alpha')
        self.configure(background='white',)

        self.geometry(f'{self.app_windows_x}x{self.app_window_y}')
        self.minsize(self.app_windows_x, self.app_window_y)
        self.maxsize(self.app_windows_x, self.app_window_y)

        barra_menus = tk.Menu()
        barra_menus.configure(background='white', borderwidth=1)
        barra_menus.add_separator()

        # me da palo inventar mas variables ma cago en la puta
        ndofsdgndfng = tk.Canvas(width=400, height=400, bg='white')
        ndofsdgndfng.place(relx=0.1,
                     rely=0.45,
                     anchor='w')


        if file_config['Base template'] != None:
            self.base_file(file_config['Base template'], False)

        if file_config['Backgrounds'] != None:
            self.backgrounds_files = file_config['Backgrounds']
            self.backgrounds()

        if file_config['Components'] != None:
            self.components_files = file_config['Components']
            self.components()

        menu_list = [{'SELECT TEMPLATE': self.add_base_file}, {'NEW BACKGROUND': self.add_background},
                     {'SET COMPONENTS TYPE': None}, {'NEW COMPONENT': None}]

        for i in range(len(menu_list)):
            for j in menu_list[i]:
                barra_menus.add_command(label=j,
                                        command=menu_list[i][j],
                                        background='white',
                                        foreground='#189AA7',
                                        activebackground='#189AA7',
                                        activeforeground='white',
                                        font=self.font_family,
                                        )

        barra_menus.add_command(label='RANDOM',
                                command=menu_list[i][j],
                                background='white',
                                foreground='GRAY',
                                activebackground='GRAY',
                                activeforeground='white',
                                font=self.font_family,
                                )

        barra_menus.add_command(label='SAVE',
                                command=menu_list[i][j],
                                background='white',
                                foreground='green',
                                activebackground='green',
                                activeforeground='white',
                                font=self.font_family,
                                )

        self.config(menu=barra_menus)

        self.text()

        ttk.Separator(
            self,
            orient='vertical',
            style='TSeparator',
            class_=ttk.Separator,
            takefocus=1,
            cursor='man'
        ).pack(fill='y', padx=10, expand=True)

    def components(self):
        c = 0.05
        for i in self.components_files:
            f = i['file']
            p = tk.Label(self, text=f'{f} :: ')
            p.config(font=self.font_family, background='white')
            p.place(relx=0.82,
                    rely=c,
                    anchor='n')

            p = tk.Label(self, text=i['type'])
            p.config(font=self.font_family, background='white')
            p.place(relx=0.91,
                    rely=c,
                    anchor='n')

            c += 0.05

    def backgrounds(self):
        c = 0.05
        for i in self.backgrounds_files:
            i = tk.Label(self, text=i)
            i.config(font=self.font_family, background='white')
            i.place(relx=0.61,
                    rely=c,
                    anchor='n')
            c += 0.05

    def add_background(self):
        filetypes = (
            ('png', '*.png'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

    def text(self):
        base = tk.Label(self, text="NFT")
        base.config(font=self.font_family, background='white')
        base.place(relx=0.25,
                   rely=0.09,
                   anchor='n')

        bks = tk.Label(self, text="BACKGROUNDS")
        bks.config(font=self.font_family, background='white')
        bks.place(relx=0.61,
                  rely=0,
                  anchor='n')

        cmts = tk.Label(self, text="COMPONENTS")
        cmts.config(font=self.font_family, background='white')
        cmts.place(relx=0.82,
                   rely=0,
                   anchor='n')

    def remove_base_template(self):
        a_file = open(file_name_config, 'w')
        file_config['Base template'] = None
        json.dump(file_config, a_file)
        a_file.close()

        self.label_image_base.after(1000, self.label_image_base.destroy())

    def base_file(self, filename, is_new) -> None:
        if is_new:
            a_file = open(file_name_config, 'w')
            file_config['Base template'] = filename
            json.dump(file_config, a_file)
            a_file.close()

        basewidth = 400
        image1 = Image.open(filename)
        wpercent = (basewidth / float(image1.size[0]))
        hsize = int((float(image1.size[1]) * float(wpercent)))
        img = image1.resize((basewidth, hsize), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)
        self.label_image_base = tk.Label(image=test)
        self.label_image_base.image = test
        self.label_image_base.place(relx=0.1,
                     rely=0.45,
                     anchor='w')

        boton = ttk.Button(text="REMOVE", command=self.remove_base_template)
        boton.place(relx=0.25,
                    rely=0.76,
                    anchor='n')

    def add_base_file(self):
        filetypes = (
            ('png', '*.png'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        self.base_file(filename, True)


app = BaseUI()
app.mainloop()

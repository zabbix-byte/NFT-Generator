import tkinter as tk
from tkinter import Button, ttk
from tkinter import filedialog as fd
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import json
import sys

file_name_config = './config_app.json'


class TKAPP(ThemedTk):
    def __init__(self) -> None:
        super().__init__()

class MenusAndHeaders:
    def __init__(self, font_f) -> None:
        self.font_family = font_f
        self.load()

    def load(self):
        barra_menus = tk.Menu()
        barra_menus.configure(background='white', borderwidth=1)
        barra_menus.add_separator()

        menu_list = [{'SELECT TEMPLATE': self.add_base_file}, {'ADD BACKGROUND': self.add_background},
                      {'ADD COMPONENT': None}]

        for i in range(len(menu_list)):
            for j in menu_list[i]:
                barra_menus.add_command(label=j,
                                        command=menu_list[i][j],
                                        background='white',
                                        foreground='#322827',
                                        activebackground='#322827',
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

class Background:
    backgrounds_list = {}
    
    def __init__(self) -> None:
        self.load()
        

    def load(self):
        c = 0.08
        file_config_e = open(file_name_config, 'r')
        file_config = json.load(file_config_e)
        file_config_e.close()

        self.backgrounds_list = {}

        if len(file_config['Backgrounds']) >  0:
            self.backgrounds_files = file_config['Backgrounds']

            for i in self.backgrounds_files:
                print(i)
                if sys.platform.lower() == 'linux':
                    p = i.split('/')[-1].split('.')[0]
                if sys.platform.lower() == 'win32':
                    p = i.split('\\')[-1].split('.')[0]

                ne_l = tk.Label(self, text=p, width=20)
                ne_l.config(font=self.font_family, background='white')
                ne_l.place(relx=0.61,
                        rely=c,
                        anchor='n')

                self.backgrounds_list[i] = ne_l

                boton = ttk.Button(self, text='X', command=lambda: self.remove_item({'Backgrounds': i}))
                boton.config(width=1)
                boton.place(relx=0.68,
                    rely=c,
                    anchor='n')
                
                self.backgrounds_list[f'{i}_btn'] = boton

                c += 0.05

class BaseUI(TKAPP, MenusAndHeaders, Background):
    def __init__(self) -> None:
        self.font_family = ('Inter', 11)

        TKAPP.__init__(self)
        MenusAndHeaders.__init__(self, self.font_family)
        Background.__init__(self)
        
        self.app_windows_x = 1280
        self.app_window_y = 720
        self.theme = 'yaru'

        self.title('NFT Generator Alpha')
        self.configure(background='white',)

        self.geometry(f'{self.app_windows_x}x{self.app_window_y}')
        self.minsize(self.app_windows_x, self.app_window_y)
        self.maxsize(self.app_windows_x, self.app_window_y)

       

        # me da palo inventar mas variables ma cago en la puta
        ndofsdgndfng = tk.Canvas(width=400, height=400, bg='white')
        ndofsdgndfng.place(relx=0.1,
                     rely=0.45,
                     anchor='w')
    

        file_name_config = './config_app.json'
        file_config_e = open(file_name_config, 'r')
        file_config = json.load(file_config_e)
        file_config_e.close()

        if file_config['Base template'] != None:
            self.base_file(file_config['Base template'], False)
    

        if file_config['Components'] != None:
            self.components_files = file_config['Components']
            self.components()

    
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
        c = 0.08
        for i in self.components_files:
            f = i['file']

            if sys.platform.lower() == 'linux':
                f = f.split('/')[-1].split('.')[0]
            if sys.platform.lower() == 'win32':
                f = f.split('\\')[-1].split('.')[0]

            p = tk.Label(self, text=f'{f}', width=30, height=1)
            p.config(font=self.font_family, background='white')
            p.place(relx=0.82,
                    rely=c,
                    anchor='n')

            typ = i['type']
            p = tk.Label(self, text=f'::    {typ}')
            p.config(font=self.font_family, background='white')
            p.place(relx=0.90,
                    rely=c,
                    anchor='n')

            boton = ttk.Button(self, text="X", command=lambda: self.remove_item(f), )
            boton.config(width=1)
            boton.place(relx=0.95,
                   rely=c,
                   anchor='n')

            c += 0.05
        

    def add_background(self):
        file_config_e = open(file_name_config, 'r')
        file_config = json.load(file_config_e)
        file_config_e.close()
        filetypes = (
            ('png', '*.png'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilenames(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        filename = self.tk.splitlist(filename)

        if len(filename) > 0:
            a_file = open(file_name_config, 'w')
            for i in filename:
                file_config['Backgrounds'].append(i)
            json.dump(file_config, a_file)
            a_file.close()
            self.backgrounds()

    def text(self):
        base = tk.Label(self, text="NFT")
        base.config(font=self.font_family, background='#322827', foreground='white')
        base.place(relx=0.25,
                   rely=0.09,
                   anchor='n')


        bks = tk.Label(self, text="BACKGROUNDS")
        bks.config(font=self.font_family, background='#322827', foreground='white')
        bks.place(relx=0.63,
                  rely=0.01,
                  anchor='n')

        cmts = tk.Label(self, text="COMPONENTS")
        cmts.config(font=self.font_family, background='#322827', foreground='white')
        cmts.place(relx=0.87,
                   rely=0.01,
                   anchor='n')
        
        cmts = tk.Label(self, text="COMPONENTS TYPES")
        cmts.config(font=self.font_family, background='#322827', foreground='white')
        cmts.place(relx=0.65,
                   rely=0.5,
                   anchor='n')
        
        entry = ttk.Entry()
        entry.place(relx=0.80,
                   rely=0.503,
                   anchor='n')

        boton = ttk.Button(text="Create Type", command=self.remove_base_template)
        boton.place(relx=0.9,
                    rely=0.498,
                    anchor='n')

    def remove_item(self, metadata):
        file_config_e = open(file_name_config, 'r')
        file_config = json.load(file_config_e)
        file_config_e.close()
        a_file = open(file_name_config, 'w')
        try:
            file_config[list(metadata.keys())[0]].remove(metadata[list(metadata.keys())[0]])
        except:
            pass
        json.dump(file_config, a_file)
        a_file.close()

        if 'Backgrounds' == list(metadata.keys())[0]:    
            self.backgrounds_list[metadata[list(metadata.keys())[0]]].after(100, self.backgrounds_list[metadata[list(metadata.keys())[0]]].destroy())
            self.backgrounds_list[f'{metadata[list(metadata.keys())[0]]}_btn'].after(100, self.backgrounds_list[f'{metadata[list(metadata.keys())[0]]}_btn'].destroy())

            self.backgrounds_list.pop(metadata[list(metadata.keys())[0]])
            self.backgrounds_list.pop(f'{metadata[list(metadata.keys())[0]]}_btn')

            self.backgrounds()

    def remove_base_template(self):
        file_config_e = open(file_name_config, 'r')
        file_config = json.load(file_config_e)
        file_config_e.close()
        a_file = open(file_name_config, 'w')
        file_config['Base template'] = None
        json.dump(file_config, a_file)
        a_file.close()

        self.label_image_base.after(1000, self.label_image_base.destroy())

    def base_file(self, filename, is_new) -> None:
        if is_new:
            file_config_e = open(file_name_config, 'r')
            file_config = json.load(file_config_e)
            file_config_e.close()
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
        if len(filename) > 1:
            self.base_file(filename, True)







    
class App(BaseUI):
    def __init__(self) -> None:
        super().__init__()

app = App()
app.mainloop()

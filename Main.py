from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Randomizer import Randomizer
import json

with open('gun_attachments.json') as w:
    weapons = json.load(w)
root = Tk()

#initial Labels to be destroyed
attach = Label(root)
perk = Label(root)
lethal = Label(root)
tactical = Label(root)

class Main:
    def __init__(self, root):
        self.root = root
        root.title("CoD Loadout: Randomizer")
        root.resizable(0,0)
        root.configure(bg='gray12')
        root.geometry("670x480")

        # Banner Image
        load = Image.open('banner.png').resize((665, 150), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        banner = Label(root, image=render, relief='flat', bg='gray12')
        banner.image = render
        banner.grid(row=0, columnspan=5, pady=(0, 10))

        # All of the methods are called here
        self.combotypes()
        self.comboguns()
        self.output_frame()
        Main.destroy_all()
    
    @staticmethod
    def destroy_all():
        """
        This method cleans up the output frame
        """

        attach.destroy()
        perk.destroy()
        lethal.destroy()
        tactical.destroy()

    def get_loadout(self):
        """
        This function returns the class that gets randomized

        The if statement is not necessary but is added just incase there are any weapons
        not in the list
        """

        if self.selection.get() in weapons:
            self.loadout = Randomizer(self.selection.get(), 'Perks', 'Lethals', 'Tacticals')
            return self.loadout
  
    def output_frame(self):
        """
        This is the output frame where all the buttons are placed as well as the
        settings for their output

        This is also where the buttons are placed and the command methods that
        are being called so they all are in the same function
        """

        self.mainframe = LabelFrame(root, width=385, height=230, bg='gray21', relief='solid')
        self.mainframe.grid_propagate(0)
        self.mainframe.grid(row=3, column=1, rowspan=5, columnspan=3)

        self.buttonframe = LabelFrame(root, width=200, height=230, bg='gray12', relief='flat')
        self.buttonframe.grid_propagate(0)
        self.buttonframe.grid(row=3, column=0, pady=(5, 0))

        def onclick_attachments():
            global attach
            attach.destroy()
            attach = Label(self.mainframe, text=self.get_loadout().a_randomize(), bg='gray21', fg='#FFFFFF')
            attach.place(x=95, y=80, anchor=CENTER)
            return attach
           
        def onclick_perks():
            global perk
            perk.destroy()
            perk = Label(self.mainframe, text=self.get_loadout().p_randomize(), bg='gray21', fg='#FFFFFF')
            perk.place(x=280, y=80, anchor=CENTER)
            return perk

        def onclick_lethals():
            global lethal
            lethal.destroy()
            lethal = Label(self.mainframe, text=self.get_loadout().l_randomize(), bg='gray21', fg='#FFFFFF')
            lethal.place(x=94, y=190, anchor=CENTER)
            return lethal

        def onclick_tacticals():
            global tactical
            tactical.destroy()
            tactical = Label(self.mainframe, text=self.get_loadout().t_randomize(), bg='gray21', fg='#FFFFFF')
            tactical.place(x=279, y=190, anchor=CENTER)
            return tactical

        # On Hover Button Events
        def on_hover_a(event):
            random_attachment_button['background'] = 'burlywood3'
        def off_hover_a(event):
            random_attachment_button['background'] = 'burlywood4'
        def on_hover_b(event):
             random_perk_button['background'] = 'burlywood3'
        def off_hover_b(event):
            random_perk_button['background'] = 'burlywood4'
        def on_hover_c(event):
            random_lethal_button['background'] = 'burlywood3'
        def off_hover_c(event):
            random_lethal_button['background'] = 'burlywood4'
        def on_hover_d(event):
            random_tactical_button['background'] = 'burlywood3'
        def off_hover_d(event):
            random_tactical_button['background'] = 'burlywood4'
        def on_hover_e(event):
            random_all_button['background'] = 'orangered3'
        def off_hover_e(event):
            random_all_button['background'] = 'orangered4'
            
        # Output Titles
        label_attach = Label(self.mainframe, font=('Fixedsys', 4), text="Use these attachments:", bg='gray21', fg='peach puff')
        label_attach.grid(row=1, column=1, padx=(10,0), pady=(10,100))
        label_perk = Label(self.mainframe, font=('Fixedsys', 4), text="Use these perks:", bg='gray21', fg='peach puff')
        label_perk.grid(row=1, column=2, pady=(10,100))
        label_lethal = Label(self.mainframe, font=('Fixedsys', 4), text="Use this for lethal:", bg='gray21', fg='peach puff')
        label_lethal.grid(row=2, column=1)
        label_tactical = Label(self.mainframe, font=('Fixedsys', 4), text="Use this for tactical:", bg='gray21', fg='peach puff')
        label_tactical.grid(row=2, column=2)

        # Randomize Attachment Button
        random_attachment_button = Button(self.buttonframe, bg='burlywood4', font=5, text="Randomize Attachments", width=20, height=2, \
            command=onclick_attachments, fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        random_attachment_button.bind('<Enter>', on_hover_a)
        random_attachment_button.bind('<Leave>', off_hover_a)
        random_attachment_button.grid(row=3, column=0, padx=(10, 0))

        # Randomize Perk Button
        random_perk_button = Button(self.buttonframe, font=5, text="Randomize Perks", width=20, height=2, \
            command=onclick_perks, bg='burlywood4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        random_perk_button.bind('<Enter>', on_hover_b)
        random_perk_button.bind('<Leave>', off_hover_b)
        random_perk_button.grid(row=4, column=0, padx=(10, 0))

        # Randomize Lethal Button
        random_lethal_button = Button(self.buttonframe, font=5, text="Randomize Lethal", width=20, height=2, \
            command=onclick_lethals, bg='burlywood4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        random_lethal_button.bind('<Enter>', on_hover_c)
        random_lethal_button.bind('<Leave>', off_hover_c)
        random_lethal_button.grid(row=5, column=0, padx=(10, 0))

        # Randomize Tactical Button
        random_tactical_button = Button(self.buttonframe, font=5, text="Randomize Tactical", width=20, height=2, \
            command=onclick_tacticals, bg='burlywood4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        random_tactical_button.bind('<Enter>', on_hover_d)
        random_tactical_button.bind('<Leave>', off_hover_d)
        random_tactical_button.grid(row=6, column=0, padx=(10, 0))

        # Randomize All Button
        random_all_button = Button(self.buttonframe, font=5, text="Randomize All", width=20, height=2, \
            command=lambda:[onclick_attachments(), onclick_perks(), onclick_lethals(), onclick_tacticals()], \
                bg='darkorange4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='orangered4', activeforeground='#FFFFFF')
        random_all_button.bind('<Enter>', on_hover_e)
        random_all_button.bind('<Leave>', off_hover_e)
        random_all_button.grid(row=7, column=0, padx=(10, 0))

    def combotypes(self):
        """
        Dropdown menu for choosing your weapon tyoe

        """

        def callback(event):
            pass

        self.select = StringVar()
        label = Label(root, font=('Fixedsys', 15), text="Choose the weapon type: ", bg='gray12', fg='peach puff')
        label.grid(row=2, column=0, pady=(0,30))
        gun_types = ttk.Combobox(root, textvariable=self.select)
        gun_types['value'] = ['Assault Rifle', 'SMG', 'Shotgun']
        gun_types.current(0)
        gun_types.bind("<<ComboboxSelected>>", callback)
        gun_types.grid(row=2, column=1, pady=(0,30))

    def comboguns(self):
        """
        Dropdown menu for choosing your weapon

        """

        def callback(event):
            Main.destroy_all()
            event.widget.get()

        self.selection = StringVar()
        label = Label(root, font=('Fixedsys', 15), text="Choose your weapon: ", bg='gray12', fg='peach puff')
        label.grid(row=2, column=2, padx=(10, 0), pady=(0,30))
        guns = ttk.Combobox(root, textvariable=self.selection)
        guns['value'] = list(gun for gun in weapons)
        guns.current(0)
        guns.bind("<<ComboboxSelected>>", callback)
        guns.grid(row=2, column=3, padx=(0,10), pady=(0,30))

output = Main(root)
root.mainloop()
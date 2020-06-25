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
        root.geometry("668x480")


        load = Image.open('banner.png').resize((665, 150), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        banner = Label(root, image=render, relief='flat', bg='gray12')
        banner.image = render
        banner.grid(row=0, columnspan=5, pady=(0, 10))

        #all frames are called here
        self.combotypes()
        self.comboguns()
        self.out_frame()
        self.rand_all()

        Main.destroy_all()
    
    @staticmethod
    def destroy_all():
        attach.destroy()
        perk.destroy()
        lethal.destroy()
        tactical.destroy()

    def combotypes(self):
        """
        Dropdown menu for choosing your weapon

        """
        def callback(event):
            pass

        self.select = StringVar()
        
        label = Label(root, font=('Fixedsys', 15), text="Choose weapon type: ", bg='gray12', fg='peach puff')
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

    def get_loadout(self):
        """
        This function returns the loadout that gets randomized
        """
        if self.selection.get() in weapons:
            self.loadout = Randomizer(self.selection.get(), 'Perks', 'Lethals', 'Tacticals')
            return self.loadout
  
    def out_frame(self):
        self.mainframe = LabelFrame(root, width=383, height=243, relief='solid')
        self.mainframe.grid_propagate(0)
        self.mainframe.grid(row=3, column=1, rowspan=5, columnspan=3)
        self.at_frame()
        self.perk_frame()
        self.lethal_frame()
        self.tactical_frame()
           
    def at_frame(self):
        """
        attachment frame
        the attachment button, labels are in this frame
        """
        frame = LabelFrame(self.mainframe, width=190, height=150, bg='gray21', relief='flat', highlightbackground='gray21')
        frame.grid_propagate(0)
        frame.grid(row=1, column=1)

        def onclick_attachments():
            """
            This function is where the attachment randomizer is utilized
            This will be used as a command for the randomize attachment button
            """
            global attach
            attach.destroy()
            attach = Label(frame, text=self.get_loadout().a_randomize(), bg='gray21', fg='#FFFFFF')
            attach.place(x=90, y=70, anchor='center')
        #Label
        label_attach = Label(frame, font=('Fixedsys', 5), text="Use these attachments: ", bg='gray21', fg='peach puff')
        label_attach.grid(row=2, column=1, padx=(3, 0))

        #Randomize Attachment Button
        random_attachment = Button(root, font=5, text="Randomize Attachments", width=20, height=1, command=onclick_attachments, bg='DodgerBlue3', fg='#FFFFFF', relief='flat', highlightthickness= 0)
        random_attachment.grid(row=3, column=0, padx=(10, 0))
        return onclick_attachments()
    
    def perk_frame(self):
        """
        perks frame
        the perks button, labels are in this frame
        """
        frame = LabelFrame(self.mainframe, width=190, height=150, bg='gray21', relief='flat', highlightbackground='gray21')
        frame.grid_propagate(0)
        frame.grid(row=1, column=2)

        def onclick_perks():
            """
            This function is where the perk randomizer is utilized
            This will be used as a command for the randomize perk button
            """
            global perk
            perk.destroy()
            perk = Label(frame, text=self.get_loadout().p_randomize(), bg='gray21', fg='#FFFFFF')
            perk.place(x=90, y=70, anchor='center')
        #Label
        label_perk = Label(frame, font=('Fixedsys', 5), text="   Use these perks: ", bg='gray21', fg='peach puff')
        label_perk.grid(row=2, column=1)

        #Randomize Perk Button
        random_perk = Button(root, font=5, text="Randomize Perks", width=20, height=1, command=onclick_perks, bg='DodgerBlue3', fg='#FFFFFF', relief='flat', highlightthickness= 0)
        random_perk.grid(row=4, column=0, padx=(10, 0))
        return onclick_perks()

    def lethal_frame(self):
        """
        lethalframe
        the lethal button, labels are in this frame
        """
        frame = LabelFrame(self.mainframe, width=190, height=90, bg='gray21', relief='flat', highlightbackground='gray21')
        frame.grid_propagate(0)
        frame.grid(row=2, column=1)
        def onclick_lethals():
            """
            This function is where the lethal randomizer is utilized
            This will be used as a command for the randomize lethal button
            """
            global lethal
            lethal.destroy()
            lethal = Label(frame, text=self.get_loadout().l_randomize(), bg='gray21', fg='#FFFFFF')
            lethal.place(x=90, y=50, anchor='center')

        #Label
        label_lethal = Label(frame, font=('Fixedsys', 5), text=" Use this for lethal: ", bg='gray21', fg='peach puff')
        label_lethal.grid(row=2, column=1)
        
        #Randomize Lethal Button
        random_lethal = Button(root, font=5, text="Randomize Lethal", width=20, height=1, command=onclick_lethals, bg='DodgerBlue3', fg='#FFFFFF', relief='flat', highlightthickness= 0)
        random_lethal.grid(row=5, column=0, padx=(10, 0))

        return onclick_lethals()

    def tactical_frame(self):
        """
        tactical frame
        the tactical button, labels are in this frame
        """
        frame = LabelFrame(self.mainframe, width=190, height=90, bg='gray21', relief='flat', highlightbackground='gray21')
        frame.grid_propagate(0)
        frame.grid(row=2, column=2)

        def onclick_tacticals():
            """
            This function is where the tactical randomizer is utilized
            This will be used as a command for the randomize tactical button
            """
            global tactical
            tactical.destroy()
            tactical = Label(frame, text=self.get_loadout().t_randomize(), bg='gray21', fg='#FFFFFF')
            tactical.place(x=90, y=50, anchor='center')

        #Label
        label_tactical = Label(frame, font=('Fixedsys', 5), text="Use this for tactical:", bg='gray21', fg='peach puff')
        label_tactical.grid(row=2, column=1, padx=(2,0))

        #Randomize Tactical Button
        random_tactical = Button(root, font=5, text="Randomize tactical", width=20, height=1, command=onclick_tacticals, bg='DodgerBlue3', fg='#FFFFFF', relief='flat', highlightthickness= 0)
        random_tactical.grid(row=6, column=0, padx=(10, 0))

        return onclick_tacticals()

    def rand_all(self):
        """
        Creates a button that randomizes all four equipments
        """

        #Randomize All Button
        random_all = Button(root, font=5, text="Randomize All", command=lambda:[self.at_frame(), self.perk_frame(), self.lethal_frame(), self.tactical_frame()], width=20, height=1, bg='orangered3', fg='#FFFFFF', relief='flat', highlightthickness= 0)
        random_all.grid(row=7, column=0, padx=(10, 0))

output = Main(root)
root.mainloop()
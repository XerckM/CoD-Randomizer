from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Randomizer import Randomizer
import json

root = Tk()

#initial Labels to be destroyed
attach = Label(root)
perk = Label(root)
lethal = Label(root)
tactical = Label(root)

with open('gun_attachments.json') as w:
    weapons = json.load(w)

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
        self.output_frame()
        self.combobox()
        self.blink_type_label()
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
        loadout = Randomizer(self.select.get(), self.selection.get(), 'Perks', 'Lethals', 'Tacticals')
        return loadout
  
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
            if self.random_attachment_button['state'] == NORMAL:
                self.random_attachment_button['background'] = 'burlywood3'
        def off_hover_a(event):
            if self.random_attachment_button['state'] == NORMAL:
                self.random_attachment_button['background'] = 'burlywood4'
        def on_hover_b(event):
            if self.random_perk_button['state'] == NORMAL:
                self.random_perk_button['background'] = 'burlywood3'
        def off_hover_b(event):
            if self.random_perk_button['state'] == NORMAL:
                self.random_perk_button['background'] = 'burlywood4'
        def on_hover_c(event):
            if self.random_lethal_button['state'] == NORMAL:
                self.random_lethal_button['background'] = 'burlywood3'
        def off_hover_c(event):
            if self.random_lethal_button['state'] == NORMAL:
                self.random_lethal_button['background'] = 'burlywood4'
        def on_hover_d(event):
            if self.random_tactical_button['state'] == NORMAL:
                self.random_tactical_button['background'] = 'burlywood3'
        def off_hover_d(event):
            if self.random_tactical_button['state'] == NORMAL:
                self.random_tactical_button['background'] = 'burlywood4'
        def on_hover_e(event):
            if self.random_all_button['state'] == NORMAL:
                self.random_all_button['background'] = 'orangered3'
        def off_hover_e(event):
            if self.random_all_button['state'] == NORMAL:
                self.random_all_button['background'] = 'orangered4'
            
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
        self.random_attachment_button = Button(self.buttonframe, bg='burlywood4', fg='#FFFFFF', font=5, text="Randomize Attachments", width=20, height=2, \
            command=onclick_attachments, relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        self.random_attachment_button.config({"disabledforeground": "gray63"})
        self.random_attachment_button.bind('<Enter>', on_hover_a)
        self.random_attachment_button.bind('<Leave>', off_hover_a)
        self.random_attachment_button.grid(row=3, column=0, padx=(10, 0))

        # Randomize Perk Button
        self.random_perk_button = Button(self.buttonframe, font=5, text="Randomize Perks", width=20, height=2, \
            command=onclick_perks, bg='burlywood4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        self.random_perk_button.config({"disabledforeground": "gray63"})
        self.random_perk_button.bind('<Enter>', on_hover_b)
        self.random_perk_button.bind('<Leave>', off_hover_b)
        self.random_perk_button.grid(row=4, column=0, padx=(10, 0))

        # Randomize Lethal Button
        self.random_lethal_button = Button(self.buttonframe, font=5, text="Randomize Lethal", width=20, height=2, \
            command=onclick_lethals, bg='burlywood4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        self.random_lethal_button.config({"disabledforeground": "gray63"})
        self.random_lethal_button.bind('<Enter>', on_hover_c)
        self.random_lethal_button.bind('<Leave>', off_hover_c)
        self.random_lethal_button.grid(row=5, column=0, padx=(10, 0))

        # Randomize Tactical Button
        self.random_tactical_button = Button(self.buttonframe, font=5, text="Randomize Tactical", width=20, height=2, \
            command=onclick_tacticals, bg='burlywood4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='tan4', activeforeground='#FFFFFF')
        self.random_tactical_button.config({"disabledforeground": "gray63"})
        self.random_tactical_button.bind('<Enter>', on_hover_d)
        self.random_tactical_button.bind('<Leave>', off_hover_d)
        self.random_tactical_button.grid(row=6, column=0, padx=(10, 0))

        # Randomize All Button
        self.random_all_button = Button(self.buttonframe, font=5, text="Randomize All", width=20, height=2, \
            command=lambda:[onclick_attachments(), onclick_perks(), onclick_lethals(), onclick_tacticals()], \
                bg='orangered4', fg='#FFFFFF', relief='flat', highlightthickness= 0, bd=0, activebackground='#621b00', activeforeground='#FFFFFF')
        self.random_all_button.config({"disabledforeground": "gray63"})
        self.random_all_button.bind('<Enter>', on_hover_e)
        self.random_all_button.bind('<Leave>', off_hover_e)
        self.random_all_button.grid(row=7, column=0, padx=(10, 0))
        self.disable_buttons()
    
    def disable_buttons(self):
        self.random_attachment_button.configure(state=DISABLED)
        self.random_perk_button.configure(state=DISABLED)
        self.random_lethal_button.configure(state=DISABLED)
        self.random_tactical_button.configure(state=DISABLED)
        self.random_all_button.configure(state=DISABLED)

    def enable_buttons(self):
        self.random_attachment_button.configure(state=NORMAL)
        self.random_perk_button.configure(state=NORMAL)
        self.random_lethal_button.configure(state=NORMAL)
        self.random_tactical_button.configure(state=NORMAL)
        self.random_all_button.configure(state=NORMAL)

    def combobox(self):
        """
        Creates two comboboxes for selection of gun type and gun

        """
        def callback_type(event):
            Main.destroy_all()
            update_box = list(gun for gun in weapons[self.select.get()][0])
            self.guns.config(state='readonly', value=update_box)
            self.guns.set('----Select Gun----')
            self.disable_buttons()
            if self.do_blink is True:
                self.blink_wep_label()
                self.do_blink = False
                self.no_blink = True

        def callback_weapon(event):
            Main.destroy_all()
            self.enable_buttons()
            self.do_blink = True
        
        self.do_blink = True
        self.no_blink = False
        self.select = StringVar()
        self.type_label = Label(root, font=('Fixedsys', 15), text="Choose the weapon type:", background='gray12', foreground='peach puff')
        self.type_label.grid(row=2, column=0, pady=(0,30))
        self.gun_types = ttk.Combobox(root, width=21, textvariable=self.select, state='readonly')
        self.gun_types['value'] = list(item for item in weapons)
        self.gun_types.set('--Select Weapon Type--')
        self.gun_types.bind("<<ComboboxSelected>>", callback_type)
        self.gun_types.grid(row=2, column=1, pady=(0,30))

        self.selection = StringVar()
        self.wep_label = Label(root, font=('Fixedsys', 15), text="Choose your weapon:", bg='gray12', fg='peach puff')
        self.wep_label.grid(row=2, column=2, padx=(10, 0), pady=(0,30))
        self.guns = ttk.Combobox(root, width=15, textvariable=self.selection, state='disabled')
        self.guns.set('---Unavailable---')
        self.guns.bind("<<ComboboxSelected>>", callback_weapon)
        self.guns.grid(row=2, column=3, padx=(0,10), pady=(0,30))

    def blink_type_label(self):
        if self.no_blink is True:
            self.type_label.after_cancel(self.blink_type_label)
            self.type_label.configure(background='gray12', foreground='peach puff')
        else:
            bg = self.type_label.cget("background")
            fg = self.type_label.cget("foreground")
            self.type_label.configure(background=fg, foreground=bg)
            self.type_label.after(350, self.blink_type_label)

    def blink_wep_label(self):
        if self.random_all_button['state'] == DISABLED:
            bg = self.wep_label.cget("background")
            fg = self.wep_label.cget("foreground")
            self.wep_label.configure(background=fg, foreground=bg)
            self.wep_label.after(350, self.blink_wep_label)
        else:
            self.wep_label.after_cancel(self.blink_wep_label)
            self.wep_label.configure(background='gray12', foreground='peach puff')

Main(root)
root.mainloop()
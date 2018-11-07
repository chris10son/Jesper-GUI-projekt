from tkinter import *
from tkinter.colorchooser import askcolor


class PaintwithJesper(object):

    Pen_Size = 5.0
    Default_Color = 'black'

#gör  knapparna  pen, color & eraser, sedan en canvas, och en scale som gör att användaren får välja storlek på  pen & eraser
    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.color_button = Button(self.root, text='Color', command=self.choose_color)
        self.color_button.grid(row=0, column=1)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()
    #setup för när man skall använda pen vid start av programmet
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.Default_Color
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
    #använd pen
    def use_pen(self):
        self.activate_button(self.pen_button)

    #Gör color ändring  tillgänglig  för användare.  importerade  även tkinter  colorchooser så  att  askcolor  rutan skapades.
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]
    #aktiverar  eraser när  användare  vill  sudda.
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
    #Gör  så att användare  ser  det  mode de är i på  knapparna, är  erase mode igång  så är endast  erase  knappen nedtryckt,  tills  du väljer  ett  annat   mode.
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode
    #eraser har färgen vit, då bakgrunden är vit.  fill paint color ser  till  att   vald  färg fungerar.  capstyle round  tar bort mellanrum.
    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color, capstyle=ROUND)
        self.old_x = event.x
        self.old_y = event.y
    #Reset
    def reset(self, event):
        self.old_x, self.old_y = None, None



PaintwithJesper()
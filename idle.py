from itertools import cycle
import tkinter as tk

#root = Tk()

list1=["idle_movements\cinigatchi_sprites\ciniidle2.PNG","idle_movements\cinigatchi_sprites\ciniidle1.PNG"]

class Idle(tk.Tk):
    ##creates idle class
    def __init__(self, list1, x, y, delay):
        ##self is root, list1 is what it cycles through, x-y adjust to window size, delay is delay
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in list1)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
    def CycleImg(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.CycleImg)
    def run(self):
        self.mainloop()

delay = 2000
#miliseconds
x = 100
y = 50

app = Idle(list1, x, y, delay)
app.CycleImg()
app.run()

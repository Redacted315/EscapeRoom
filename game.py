import tkinter as tk
# from tkinter import *


class Fullscreen_Window:

    def __init__(self):
        self.root = tk.Tk()

        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.counter = 10
        self.timer_label = tk.Label(self.frame, text=f"{self.counter}")
        self.timer_label.pack()
        self.state = False
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<F10>", self.display_gif)
        self.root.bind("<F9>", quit)
        self.toggle_fullscreen()
        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.state)
        self.root.update()
        self.display_gif()

    def display_gif(self, event=None):
        def update(ind):
            if self.counter == 0:
                print("explpoded")
                quit()
            self.counter -= 1
            self.timer_label.config(text=f"{self.counter}")
            self.root.after(1000, update, 0)

        self.root.after(0, update, 0)


def test():
    w = Fullscreen_Window()
    # w.toggle_fullscreen()

if __name__ == '__main__':
    test()
    

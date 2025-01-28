import tkinter as tk
from tkinter.font import BOLD, Font
from datetime import datetime, timedelta

class Game():

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.timer_font = Font(self.root, size=32, weight=BOLD)
        self.entry_font = Font(self.root, size=18)
        self.timer_frame = tk.Frame(self.root)
        self.timer_frame.place(x=5, y=0)
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=30) # length of game timer
        # self.counter = 10
        self.timer_label = tk.Label(self.timer_frame, text=f"", font=self.timer_font)
        self.timer_label.pack()
        self.state = False

        # Layout
        self.entry_frame = tk.Frame(self.root)
        self.entry_1 = tk.Entry(self.entry_frame,font=self.entry_font,  width=4)
        self.dash_1 = tk.Label(self.entry_frame, font=self.entry_font, text="-")
        self.entry_2 = tk.Entry(self.entry_frame,font=self.entry_font,  width=4)
        self.dash_2 = tk.Label(self.entry_frame, font=self.entry_font, text="-")
        self.entry_3 = tk.Entry(self.entry_frame,font=self.entry_font,  width=4)

        self.entry_1.grid(column=0, row=0)
        self.dash_1.grid(column=1, row=0)
        self.entry_2.grid(column=2, row=0)
        self.dash_2.grid(column=3, row=0)
        self.entry_3.grid(column=4, row=0)
        self.pos_x = ( self.screen_width / 2 ) - ( self.entry_frame.winfo_width() / 2 )-75
        self.entry_frame.place(x=self.pos_x, y=self.screen_height/2)

        # -------------------- for testing --------------------
        self.root.bind("<F11>", self.toggle_fullscreen) #     |
        self.root.bind("<F10>", self.countdown) #             |
        self.root.bind("<Escape>", quit) #                    |
        # -----------------------------------------------------
        self.toggle_fullscreen()
        self.root.mainloop()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # toggle boolean
        self.root.attributes("-fullscreen", self.state)
        self.root.update()
        
        self.countdown()

    def countdown(self, event=None):
        def update(ind):

            time_left = (self.end_time - datetime.now()).total_seconds()
            self.timer_label.config(text=f"{int((time_left%3600)//60)}:{int(time_left%60)}")
            self.root.after(1000, update, 0)

        self.root.after(0, update, 0)


def test():
    w = Game()

if __name__ == '__main__':
    test()
    

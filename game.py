import tkinter as tk
from tkinter.font import BOLD, Font
from datetime import datetime, timedelta
from pygame import mixer  # Used for audio playback.

class Game():

    def __init__(self, root: tk.Tk) -> None:
        hint_file = ["assets\\audio\\hint_1.mp3", "assets\\audio\\hint_2.mp3", "assets\\audio\\hint_3.mp3", "assets\\audio\\hint_4.mp3"]
        mixer.init()
        self.hints = []
        # self.sound_wrong = mixer.Sound("assets\\audio\\wrong.mp3")
        for hint in hint_file:
            self.hints.append(mixer.Sound(hint))
        self.root = root
        self.root.configure(background="#303030")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.timer_font = Font(self.root, size=32, weight=BOLD)
        self.entry_font = Font(self.root, size=18)
        self.timer_frame = tk.Frame(self.root)
        self.timer_frame.place(x=5, y=0)
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=1) # length of game timer
        # self.counter = 10
        self.timer_label = tk.Label(self.timer_frame, text=f"", font=self.timer_font)
        self.timer_label.pack()
        self.state = False

        # Layout
        self.entry_frame = tk.Frame(self.root) # 870px wide
        self.entry_text_1 = tk.StringVar()
        self.entry_text_2 = tk.StringVar()
        self.entry_text_3 = tk.StringVar()
        self.entry_text_4 = tk.StringVar()
        self.entry_1 = tk.Entry(self.entry_frame,font=self.entry_font, textvariable=self.entry_text_1, width=4)
        self.dash_1 = tk.Label(self.entry_frame, font=self.entry_font, text="-")
        self.entry_2 = tk.Entry(self.entry_frame,font=self.entry_font, textvariable=self.entry_text_2,  width=4)
        self.dash_2 = tk.Label(self.entry_frame, font=self.entry_font, text="-")
        self.entry_3 = tk.Entry(self.entry_frame,font=self.entry_font, textvariable=self.entry_text_3,  width=4)
        self.dash_3 = tk.Label(self.entry_frame, font=self.entry_font, text="-")
        self.entry_4 = tk.Entry(self.entry_frame,font=self.entry_font, textvariable=self.entry_text_4,  width=4)

        self.entry_1.grid(column=0, row=0, padx=75)
        self.dash_1.grid(column=1, row=0)
        self.entry_2.grid(column=2, row=0, padx=75)
        self.dash_2.grid(column=3, row=0)
        self.entry_3.grid(column=4, row=0, padx=75)
        self.dash_3.grid(column=5, row=0)
        self.entry_4.grid(column=6, row=0, padx=75)
        self.pos_x = ( self.screen_width / 2 ) - ( 870 / 2 ) # self.entry_frame.winfo_width() wasnt working idk why
        self.entry_frame.place(x=self.pos_x, y=self.screen_height/2)

        self.hint_frame = tk.Frame(self.root)
        self.hint_1 = tk.Button(self.hint_frame, text="🔉", command=lambda: self.hints[0].play())
        self.hint_2 = tk.Button(self.hint_frame, text="🔉", command=lambda: self.hints[1].play())
        self.hint_3 = tk.Button(self.hint_frame, text="🔉", command=lambda: self.hints[2].play())
        self.hint_4 = tk.Button(self.hint_frame, text="🔉", command=lambda: self.hints[3].play())
        self.hint_1.grid(column=0, row=0, padx=75)
        self.hint_2.grid(column=1, row=0, padx=75)
        self.hint_3.grid(column=2, row=0, padx=75)
        self.hint_4.grid(column=3, row=0, padx=75)
        self.hint_frame.place(x=self.pos_x, y=(self.screen_height/2)+50)
        self.submit_btn = tk.Button(self.root, text="Submit", command=self.submit).place(x=self.pos_x, y=(self.screen_height/2)+100)

        # -------------------- for testing --------------------
        self.root.bind("<F11>", self.toggle_fullscreen) #     |
        self.root.bind("<F10>", self.countdown) #             |
        self.root.bind("<Escape>", quit) #                    |
        # -----------------------------------------------------
        self.toggle_fullscreen()
        self.root.update()

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
    
    def submit(self):
        entered_pswd = f"{self.entry_1.get()}{self.entry_2.get()}{self.entry_3.get()}"
        print(entered_pswd)



# def test():
#     w = Game()


# if __name__ == '__main__':
#     test()


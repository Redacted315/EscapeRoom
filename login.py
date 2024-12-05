import tkinter as tk
import time

class Login():
    def __init__(self):
        self.is_auth = None
        self.main = tk.Tk()
        self.main.title("Login")
        self.main.resizable(width=False, height=False)
        window_width = 600
        window_height = 400
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        pos_x = ( screen_width / 2 ) - ( window_width / 2 )
        pos_y = ( screen_height / 2 ) - ( window_height / 2 )
        self.main.geometry(f"{window_width}x{window_height}+{int(pos_x)}+{int(pos_y)}")
        
        self.submit_btn = tk.Button(self.main, text="Submit", command=self.go)
        self.submit_btn.pack()
        self.main.mainloop()
    def display_gif(self, file="miku.gif"):
        frameCnt = 6
        frames = [tk.PhotoImage(file=file,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label.configure(image=frame)
            self.main.after(100, update, ind)
        label = tk.Label(self.main)
        label.pack()
        self.main.after(0, update, 0)
        # self.main.mainloop()
    def go(self):
        self.is_auth = True
        self.submit_btn.destroy()
        self.main.update()
        self.display_gif()
        # self.main.quit()


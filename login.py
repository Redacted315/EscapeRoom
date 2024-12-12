import multiprocessing
import tkinter as tk
import time

class Login():
    def __init__(self, captcha, gif_file, gif_fps):
        
        self.fps = {10:100, 15:67, 24:42 , 30:33, 36:28, 42:24}  # delay between frames in ms
        self.captcha = captcha
        self.gif_file = gif_file
        self.gif_fps = gif_fps
        self.is_auth = False
        self.main = tk.Tk()
        self.main.title("Login")
        self.main.resizable(width=False, height=False)

        window_width = 600
        window_height = 600
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        pos_x = ( screen_width / 2 ) - ( window_width / 2 )
        pos_y = ( screen_height / 2 ) - ( window_height / 2 )
        self.main.geometry(f"{window_width}x{window_height}+{int(pos_x)}+{int(pos_y)}")
        
        #self.submit_btn = tk.Button(self.main, text="Submit", command=self.go)
        
        self.picture_frame = tk.Frame(self.main)
        self.picture = tk.PhotoImage(file=self.captcha, format="png")
        self.picture_label = tk.Label(self.picture_frame, image=self.picture).pack()
        self.picture_frame.pack()

        self.digit_frame = tk.Frame(self.main)
        self.digit_1 = tk.Label(self.digit_frame, text="0").grid(column=0, row=0)
        self.digit_2 = tk.Label(self.digit_frame, text="0").grid(column=1, row=0)
        self.digit_3 = tk.Label(self.digit_frame, text="0").grid(column=2, row=0)
        self.digit_frame.pack()

        self.button_frame = tk.Frame(self.main)
        self.button_1 = tk.Button(self.button_frame, text="1", command=lambda: self.enter_number(1)).grid(column=0, row=0)
        self.button_2 = tk.Button(self.button_frame, text="2", command=lambda: self.enter_number(2)).grid(column=1, row=0)
        self.button_3 = tk.Button(self.button_frame, text="3", command=lambda: self.enter_number(3)).grid(column=2, row=0)
        self.button_4 = tk.Button(self.button_frame, text="4", command=lambda: self.enter_number(4)).grid(column=0, row=1)
        self.button_5 = tk.Button(self.button_frame, text="5", command=lambda: self.enter_number(5)).grid(column=1, row=1)
        self.button_6 = tk.Button(self.button_frame, text="6", command=lambda: self.enter_number(6)).grid(column=2, row=1)
        self.button_7 = tk.Button(self.button_frame, text="7", command=lambda: self.enter_number(7)).grid(column=0, row=2)
        self.button_8 = tk.Button(self.button_frame, text="8", command=lambda: self.enter_number(8)).grid(column=1, row=2)
        self.button_9 = tk.Button(self.button_frame, text="9", command=lambda: self.enter_number(9)).grid(column=2, row=2)
        self.button_0 = tk.Button(self.button_frame, text="0", command=lambda: self.enter_number(0)).grid(column=0, row=3)
        self.button_reset = tk.Button(self.button_frame, text="Reset", command=self.clear_nums).grid(column=2, row=3)
        self.button_frame.pack()
        self.main.mainloop()
        
    def display_gif(self): # credit to https://stackoverflow.com/a/42882481
        # file = self.gif_file
        self.n_of_loops = 0
        frameCnt = 15
        

        frames = [tk.PhotoImage(file=self.gif_file,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
        def update(ind):
            # kill window after gif loops 5 times
            if self.n_of_loops >= frameCnt*5:
                self.main.quit()

            self.n_of_loops += 1
            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label.configure(image=frame)
            self.main.after(self.fps[self.gif_fps], update, ind)
        label = tk.Label(self.main)
        label.pack()
        self.main.after(0, update, 0)
        # self.main.mainloop()
    
    def enter_number(self, b):
        print(b)
        
    def clear_nums(self):
        pass
    def go(self):
        self.is_auth = True
        self.submit_btn.destroy()
        self.main.update()
        self.display_gif()



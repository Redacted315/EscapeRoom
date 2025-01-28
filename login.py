import tkinter as tk  # Used for GUI creation.
from pygame import mixer  # Used for audio playback.

class Login():
    def __init__(self, gif_fps=15):
        # Initialize the mixer for playing sounds.
        mixer.init()
        self.sound_wrong = mixer.Sound("assets\\audio\\wrong.mp3")  # Load the 'wrong' sound.
        self.sound_right = mixer.Sound("assets\\audio\\right.mp3")  # Load the 'right' sound.
        
        # Define a mapping for frame delay based on the desired FPS for GIF animation.
        self.fps = {10: 100, 15: 67, 24: 42, 30: 33, 36: 28, 42: 24}
        self.captcha = "assets\\images\\captcha.png"  # Path to the CAPTCHA image.
        self.gif_file = "assets\\animations\\login.gif"  # Path to the GIF animation.
        self.gif_fps = gif_fps  # FPS setting for the GIF animation.
        self.is_auth = False  # Track if authentication is successful.

        # Initialize the main application window.
        self.main = tk.Tk()
        self.main.title("Login")
        self.main.resizable(width=False, height=False)
        self.main.configure(background="#36454F")  # Set background color.

        # Configure the size and position of the window.
        window_width = 600
        window_height = 725
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        pos_x = (screen_width / 2) - (window_width / 2)
        pos_y = (screen_height / 2) - (window_height / 2)
        self.main.geometry(f"{window_width}x{window_height}+{int(pos_x)}+{int(pos_y)}")

        # Create a frame to hold the CAPTCHA image.
        self.picture_frame = tk.Frame(self.main)
        self.picture = tk.PhotoImage(file=self.captcha, format="png")  # Load CAPTCHA image.
        self.picture_label = tk.Label(self.picture_frame, image=self.picture).pack()
        self.picture_frame.pack(pady=5)

        # Create a frame to display user input digits.
        self.digit_frame = tk.Frame(self.main)
        self.digit_1 = tk.Label(self.digit_frame, text="_", width=2)
        self.digit_1.grid(column=0, row=0, ipady=3)
        self.digit_2 = tk.Label(self.digit_frame, text="_", width=2)
        self.digit_2.grid(column=1, row=0, ipady=3)
        self.digit_3 = tk.Label(self.digit_frame, text="_", width=2)
        self.digit_3.grid(column=2, row=0, ipady=3)
        
        # Style the digit labels.
        for digit in [self.digit_1, self.digit_2, self.digit_3]:
            digit.config(font=("Courier", 44), background="#849884")
        self.digit_frame.configure(relief="sunken", borderwidth=4)
        self.digit_frame.pack(pady=5)

        # Create a frame for the keypad buttons.
        self.button_frame = tk.Frame(self.main)
        reset_photo = tk.PhotoImage(file="assets\\images\\reset.png")  # Load reset button image.
        enter_photo = tk.PhotoImage(file="assets\\images\\enter.png")  # Load enter button image.

        # Generate numeric buttons dynamically
        for i in range(1, 10):
            row, col = divmod(i - 1, 3)  # Adjust row and column for 1-9
            tk.Button(self.button_frame, text=str(i), command=lambda x=i: self.enter_number(x), height=3, width=5)\
                .grid(column=col, row=row, padx=5, pady=5)
        # Place the 0 button specifically in the center of the last row
        self.button_0 = tk.Button(self.button_frame, text="0", command=lambda: self.enter_number(0), height=3, width=5)
        self.button_0.grid(column=1, row=3, padx=5, pady=5)

        # Add reset and enter buttons.
        self.button_reset = tk.Button(self.button_frame, image=reset_photo, command=self.clear_nums)\
            .grid(column=0, row=3, padx=5, pady=5)
        self.button_enter = tk.Button(self.button_frame, image=enter_photo, command=self.submit)\
            .grid(column=2, row=3, padx=5, pady=5)
        self.button_frame.configure(background="#899499", relief="raised", borderwidth=4)
        self.button_frame.pack(pady=5)

        # Start the Tkinter main loop.
        self.main.mainloop()

    def display_gif(self):
        """Plays a looping GIF animation and exits after two loops."""
        self.n_of_loops = 0
        frameCnt = 15  # Number of frames in the GIF.
        
        # Load all frames of the GIF.
        frames = [tk.PhotoImage(file=self.gif_file, format=f'gif -index {i}') for i in range(frameCnt)]
        
        def update(ind):
            # Exit the application after two loops.
            if self.n_of_loops >= frameCnt * 2:
                self.main.quit()

            self.n_of_loops += 1
            label.configure(image=frames[ind])
            ind = (ind + 1) % frameCnt  # Cycle through frames.
            self.main.after(self.fps[self.gif_fps], update, ind)

        label = tk.Label(self.main)
        label.pack()
        self.main.after(0, update, 0)

    def enter_number(self, b):
        """Handles numeric input from the user."""
        for digit in [self.digit_1, self.digit_2, self.digit_3]:
            if digit["text"] == "_":
                digit.config(text=str(b))
                return

    def clear_nums(self):
        """Clears all digits."""
        for digit in [self.digit_1, self.digit_2, self.digit_3]:
            digit.config(text="_")

    def submit(self):
        """Validates the entered digits and plays success or failure feedback."""
        if self.digit_1["text"] != "4" or self.digit_2["text"] != "5" or self.digit_3["text"] != "8":
            self.sound_wrong.play()
            self.clear_nums()
        else:
            self.sound_right.play()
            self.is_auth = True
            for frame in [self.picture_frame, self.button_frame, self.digit_frame]:
                frame.destroy()
            self.main.update()
            self.display_gif()

# def test():
#     a = Login()

# if __name__ == "__main__":
#     test()
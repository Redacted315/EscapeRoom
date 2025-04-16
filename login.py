import tkinter as tk  # Used for GUI creation.
from pygame import mixer  # Used for audio playback.

class Login():
    """
    Login class creates a GUI-based login interface using Tkinter
    that accepts a 3-digit PIN input and provides audio-visual feedback.
    """

    def __init__(self, root, gif_fps=15):
        """
        Initialize the login interface with UI components and sound.
        
        Args:
            root (tk.Tk): The root window of the Tkinter application.
            gif_fps (int): Desired frame rate for GIF animation.
        """
        # Initialize the mixer for sound playback
        mixer.init()
        self.sound_wrong = mixer.Sound("assets\\audio\\wrong.mp3")  # Error sound
        self.sound_right = mixer.Sound("assets\\audio\\right.mp3")  # Success sound

        # FPS mappings to control animation speed
        self.fps = {10: 100, 15: 67, 24: 42, 30: 33, 36: 28, 42: 24}
        self.captcha = "assets\\images\\captcha.png"
        self.gif_file = "assets\\animations\\login.gif"
        self.gif_fps = gif_fps
        self.is_auth = False  # Authentication flag

        # Root window setup
        self.main = root
        self.main.title("Login")
        self.main.resizable(width=False, height=False)
        self.main.configure(background="#36454F")

        # Center the window on the screen
        window_width, window_height = 600, 725
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        pos_x = (screen_width / 2) - (window_width / 2)
        pos_y = (screen_height / 2) - (window_height / 2)
        self.main.geometry(f"{window_width}x{window_height}+{int(pos_x)}+{int(pos_y)}")

        # ---- CAPTCHA Display ----
        self.picture_frame = tk.Frame(self.main)
        self.picture = tk.PhotoImage(file=self.captcha, format="png")
        self.picture_label = tk.Label(self.picture_frame, image=self.picture).pack()
        self.picture_frame.pack(pady=5)

        # ---- Digit Display (for PIN) ----
        self.digit_frame = tk.Frame(self.main)
        self.digit_1 = tk.Label(self.digit_frame, text="_", width=2)
        self.digit_2 = tk.Label(self.digit_frame, text="_", width=2)
        self.digit_3 = tk.Label(self.digit_frame, text="_", width=2)

        # Grid layout
        self.digit_1.grid(column=0, row=0, ipady=3)
        self.digit_2.grid(column=1, row=0, ipady=3)
        self.digit_3.grid(column=2, row=0, ipady=3)

        # Style digit labels
        for digit in [self.digit_1, self.digit_2, self.digit_3]:
            digit.config(font=("Courier", 44), background="#849884")
        self.digit_frame.configure(relief="sunken", borderwidth=4)
        self.digit_frame.pack(pady=5)

        # ---- Keypad ----
        self.button_frame = tk.Frame(self.main)
        reset_photo = tk.PhotoImage(file="assets\\images\\reset.png")
        enter_photo = tk.PhotoImage(file="assets\\images\\enter.png")

        # Numeric buttons (1-9)
        for i in range(1, 10):
            row, col = divmod(i - 1, 3)
            tk.Button(
                self.button_frame,
                text=str(i),
                command=lambda x=i: self.enter_number(x),
                height=3,
                width=5
            ).grid(column=col, row=row, padx=5, pady=5)

        # Zero button centered
        self.button_0 = tk.Button(
            self.button_frame,
            text="0",
            command=lambda: self.enter_number(0),
            height=3,
            width=5
        )
        self.button_0.grid(column=1, row=3, padx=5, pady=5)

        # Reset and submit buttons
        self.button_reset = tk.Button(
            self.button_frame,
            image=reset_photo,
            command=self.clear_nums
        ).grid(column=0, row=3, padx=5, pady=5)

        self.button_enter = tk.Button(
            self.button_frame,
            image=enter_photo,
            command=self.submit
        ).grid(column=2, row=3, padx=5, pady=5)

        self.button_frame.configure(background="#899499", relief="raised", borderwidth=4)
        self.button_frame.pack(pady=5)

        self.main.mainloop()

    def display_gif(self):
        """
        Play a looping GIF animation, used after successful login.
        Closes the window after 2 loops of 15 frames.
        """
        self.n_of_loops = 0
        frameCnt = 15  # Number of frames in the GIF

        # Load all frames from the GIF file
        frames = [
            tk.PhotoImage(file=self.gif_file, format=f'gif -index {i}')
            for i in range(frameCnt)
        ]

        def update(ind):
            if self.n_of_loops >= frameCnt * 2:
                self.main.destroy()  # Close app after 2 loops

            self.n_of_loops += 1
            label.configure(image=frames[ind])
            ind = (ind + 1) % frameCnt
            self.main.after(self.fps[self.gif_fps], update, ind)

        label = tk.Label(self.main)
        label.pack()
        self.main.after(0, update, 0)

    def enter_number(self, b):
        """
        Add a digit to the next available input label.

        Args:
            b (int): The digit entered.
        """
        for digit in [self.digit_1, self.digit_2, self.digit_3]:
            if digit["text"] == "_":
                digit.config(text=str(b))
                return

    def clear_nums(self):
        """
        Clears the entered digits, resetting the digit display.
        """
        for digit in [self.digit_1, self.digit_2, self.digit_3]:
            digit.config(text="_")

    def submit(self):
        """
        Check if entered digits match the correct password (458).
        Plays success or failure sounds and proceeds accordingly.
        """
        if self.digit_1["text"] != "4" or self.digit_2["text"] != "5" or self.digit_3["text"] != "8":
            self.sound_wrong.play()
            self.clear_nums()
        else:
            self.sound_right.play()
            self.is_auth = True
            # Remove existing widgets
            for frame in [self.picture_frame, self.button_frame, self.digit_frame]:
                frame.destroy()

            # Mark user as logged in
            with open("is.loggedin", 'w') as file:
                file.write("True")

            # Play success animation
            self.display_gif()

# For testing only:
# def test():
#     root = tk.Tk()
#     a = Login(root)
#     root.mainloop()
# if __name__ == "__main__":
#     test()
import threading
import time
import tkinter as tk
from login import Login
from game import Game


def background_task(root, game):
    while True:
        with open("is_logged_in", 'r') as file:
            if file.readline() == "True":
                root.after(0, on_logged_in, root, game)
                break
        time.sleep(2)  # Wait before checking again


def on_logged_in(root, game):
    root.deiconify()
    game.begin()


def main():
    # make sure not logged in from last session
    with open("is_logged_in", 'w') as file:
        file.write("False")
    root = tk.Tk()
    toplevel = tk.Toplevel(root)
    game = Game(root)
    root.withdraw()
    # Start the background thread
    thread = threading.Thread(target=background_task, args=(root, game), daemon=True)
    thread.start()
    login = Login(toplevel)
    root.mainloop()


if __name__ == "__main__":
    main()

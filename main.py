import threading
import time
import tkinter as tk
from login import Login
from game import Game

def background_task(root, game):
    """
    Continuously checks if the login has been marked as successful.
    Once it detects a successful login, it triggers the game start.

    Args:
        root (tk.Tk): The main application window.
        game (Game): The Game object instance.
    """
    while True:
        with open("is.loggedin", 'r') as file:
            if file.readline() == "True":
                # Run the on_logged_in function on the main thread
                root.after(0, on_logged_in, root, game)
                break
        time.sleep(2)  # Poll every 2 seconds

def on_logged_in(root, game):
    """
    Callback function that is run when the user is authenticated.

    Args:
        root (tk.Tk): The main window that was hidden during login.
        game (Game): The Game instance to begin after login.
    """
    root.deiconify()  # Show the main window
    game.go()         # Start the game timer

def main():
    """
    Main function that sets up the login and game GUI components.
    It initializes the login window, starts a background task to check for
    login success, and launches the game interface when authenticated.
    """
    # Reset login state from previous session
    with open("is.loggedin", 'w') as file:
        file.write("False")

    root = tk.Tk()             # Main application window (game screen)
    toplevel = tk.Toplevel(root)  # Separate window for login
    game = Game(root)          # Instantiate the game
    root.withdraw()            # Hide the game window during login

    # Start background thread to watch login status
    thread = threading.Thread(
        target=background_task,
        args=(root, game),
        daemon=True
    )
    thread.start()

    # Start the login process (runs blocking in the toplevel window)
    login = Login(toplevel)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

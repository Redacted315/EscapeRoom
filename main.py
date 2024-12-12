import tkinter as tk
from login import Login

# to fix gif not using background
# magick input.gif -coalesce output.gif

def main():
    login = Login("miku.png", "vault.gif", 15)
    # login.main.mainloop()
    if not login.is_auth:
        print("not logged in")
    else:
        print("logged in")


if __name__ == "__main__":
    main()

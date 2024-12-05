import tkinter as tk
from login import Login



def main():
    login = Login()
    # login.main.mainloop()
    if not login.is_auth:
        print("not logged in")
    else:
        print("logged in")


main()
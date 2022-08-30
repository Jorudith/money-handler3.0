# import gui module (tk)
from tkinter import Tk
from tkinter import ttk

# import dependencies
import json
import funcs
import logger

with open("json/app_settings.json", "r") as file:
    AS = dict(json.load(file))

root = Tk()
root.title(AS.get("app_title"))
root.iconbitmap("img/favicon.ico")
root.geometry(f"{AS.get('app_width')}x{AS.get('app_height')}")
root.resizable(AS.get("app_isresizeable"), AS.get("app_isresizeable"))
root.configure(bg=AS.get("app_bg"))

left_frame = ttk.Frame(root, width=100, height=100)
right_frame = ttk.Frame(root, width=100, height=100)

left_frame.place(x=0, y=0)
right_frame.place(x=101, y=0)


root.mainloop()
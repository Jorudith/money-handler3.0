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

left_frame = ttk.Frame(root, width=155, height=790)
right_frame = ttk.Frame(root, width=830, height=790)

left_frame.place(x=5, y=5)
right_frame.place(x=165, y=5)

main_title = ttk.Label(left_frame, text="Money Handler", font=("Bahnschirft", 10))

main_title.place(x=0, y=0)

root.mainloop()
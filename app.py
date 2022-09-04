# import gui module (tk)
import tkinter as tk

# import dependencies
import json
import funcs
import logger

with open("json/app_settings.json", "r") as file:
    AS = dict(json.load(file))

root = tk.Tk()
root.title(AS.get("app_title"))
root.iconbitmap("img/favicon.ico")
root.geometry(f"{dict(AS.get('app_width')).get('default')}x{dict(AS.get('app_height')).get('default')}")
root.minsize(width=dict(AS.get('app_width')).get('min'), height=dict(AS.get('app_height')).get('min'))
root.maxsize(width=dict(AS.get('app_width')).get('max'), height=dict(AS.get('app_height')).get("max"))
root.resizable(AS.get("app_isresizeable"), AS.get("app_isresizeable"))
root.configure(bg=AS.get("app_bg"))

# border initialization
top_border = tk.Frame(root, background="#dddddd", width=10, height=10)
center_border = tk.Frame(root, background="#dddddd", width=10, height=10)
bot_border = tk.Frame(root, background="#dddddd", width=10, height=10)
left_border = tk.Frame(root, background="#dddddd", width=10, height=10)
right_border = tk.Frame(root, background="#dddddd", width=10, height=10)

# main frame initialization
side_frame = tk.Frame(root, background="gray", width=10, height=800)
main_frame = tk.Frame(root, background="#14ee14", width=10, height=800)

# border grid
top_border.grid(row=0, column=0, columnspan=4)
center_border.grid(row=0, column=2, sticky="ns")
bot_border.grid(row=2, column=0, columnspan=4)
left_border.grid(row=0, column=0, rowspan=2)
right_border.grid(row=0, column=4, rowspan=2)

# main frame grid
side_frame.grid(row=1, column=1, sticky="nsew")
main_frame.grid(row=1, column=3, sticky="nsew")

# column weight configuration (for flexibility)
root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=8)

# row weight configuration (for flexibility)
root.rowconfigure(1, weight=1)

# side_frame child (button/label) initialization
add_button = tk.Button(side_frame, text="ADD FUNDS")

root.mainloop()
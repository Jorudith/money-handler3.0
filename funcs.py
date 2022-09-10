# import tkinter for function purposes
import tkinter as tk

# import the main logger
from logger import logger, current_year

# app function logger
def func_log(function):
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
            logger.debug(f"{function} has been used")
        except:
            logger.warning(f"{function} Something we don't know went wrong")
    return wrapper

def start():
    pass

def hover(event, widget: tk.Label | tk.Frame | tk.Button):
    widget.configure(fg="#ffffff")

def unhover(event, widget: tk.Label | tk.Frame | tk.Button):
    widget.configure(fg="#31ff93")

def home(event, master: tk.Tk, *slaves) -> None:
    for child in master.winfo_children():
        child.grid_forget()
        
    pos = 0
    max_children = 2
    while pos != max_children:
        master.winfo_children()[pos].grid(row=pos, column=0, pady=8, sticky="ew", columnspan=2)
        pos += 1

    master.columnconfigure(0, weight=1)
    master.rowconfigure(0, weight=0)
    master.rowconfigure(1, weight=0)

def manage_funds(master: tk.Tk, section: str, *slaves) -> None:
    for child in master.winfo_children():
        child.grid_forget()
    
    if section == "addfunds":
        master.winfo_children()[2].grid(row=0, column=0, pady=(5, 0), sticky="sew", columnspan=2)
        master.winfo_children()[3].grid(row=1, column=0, pady=5, sticky="e")
        master.winfo_children()[4].grid(row=1, column=1, pady=5, sticky="w")
        master.winfo_children()[5].grid(row=2, column=0, pady=5, sticky="e")
        master.winfo_children()[6].grid(row=2, column=1, pady=5, sticky="w")
        master.winfo_children()[7].grid(row=3, column=0, pady=(5, 25), columnspan=2)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(8, weight=0)



    elif section == "deductfunds":
        master.winfo_children()[8].grid(row=0, column=0, pady=(5, 0))
        master.winfo_children()[9].grid(row=1, column=0, pady=5)
        master.winfo_children()[10].grid(row=2, column=0, pady=5)
        master.winfo_children()[11].grid(row=3, column=0, pady=5)
        master.winfo_children()[12].grid(row=4, column=0, pady=5)
        master.winfo_children()[13].grid(row=5, column=0, pady=5)
        master.winfo_children()[14].grid(row=6, column=0, pady=5)
        master.winfo_children()[15].grid(row=7, column=0, pady=5)

        master.winfo_children()[16].grid(row=8, column=0, pady=(5, 0), sticky="sew", columnspan=2)
        master.winfo_children()[17].grid(row=9, column=0, pady=5, sticky="e")
        master.winfo_children()[18].grid(row=9, column=1, pady=5, sticky="w")
        master.winfo_children()[19].grid(row=10, column=0, pady=5, sticky="e")
        master.winfo_children()[20].grid(row=10, column=1, pady=5, sticky="w")
        master.winfo_children()[21].grid(row=11, column=0, pady=(5, 25), columnspan=2)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=2)
        master.rowconfigure(0, weight=0)
        master.rowconfigure(8, weight=1)

def fixed_comment():
    #TODO tk radiobuttons
    pass

def check_funds() -> str:
    with open(f"log/{current_year} logs/transactions.log") as file:
        logs = file.read()
        if logs.find("+") == -1:
            return "NO FUNDS ADDED"
        else:
            return f"${logs[logs.rindex('+')+1:]}"

@func_log
def submit_funds(amount) -> None:
    pass

@func_log
def check_logs(master: tk.Tk) -> None:
    pass


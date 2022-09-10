# import gui module (tk)
import tkinter as tk

# import dependencies
from json import load as jsonload
import funcs
from logger import logger

with open("json/app_settings.json", "r") as file:
    AS = dict(jsonload(file))

root = tk.Tk()
root.title(AS.get("app_title"))
root.iconbitmap("img/favicon2.0.ico")
root.geometry(f"{dict(AS.get('app_width')).get('default')}x{dict(AS.get('app_height')).get('default')}")
root.minsize(width=dict(AS.get('app_width')).get('min'), height=dict(AS.get('app_height')).get('min'))
root.maxsize(width=dict(AS.get('app_width')).get('max'), height=dict(AS.get('app_height')).get("max"))
root.resizable(AS.get("app_isresizeable"), AS.get("app_isresizeable"))
root.configure(bg=AS.get("app_bg"))

# main frame initialization
side_frame = tk.Frame(root, background="#999999", highlightbackground="#555555", highlightthickness=4)
main_frame = tk.Frame(root, background="#31b573", highlightbackground="#555555", highlightthickness=4)

# main frame grid
side_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid(row=0, column=1, sticky="nsew")

# column weight configuration (for flexibility) 
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

# row weight configuration (for flexibility)
root.rowconfigure(0, weight=1)

# side_frame child (button/label) initialization
title_label = tk.Label(side_frame, text="MONEY HANDLER", fg="#31ff93", bg="#999999", font=("Bahnschrift", 17), cursor="hand2")
add_button = tk.Button(side_frame, text="ADD FUNDS", fg="#ffffff", bg="#31b573", bd=1, pady=5, command=lambda: funcs.manage_funds(main_frame, "addfunds"), activebackground="#999999")
deduct_button = tk.Button(side_frame, text="DEDUCT FUNDS", fg="#ffffff", bg="#31b573", bd=1, pady=5, command=lambda: funcs.manage_funds(main_frame, "deductfunds"), activebackground="#999999")
checklog_button = tk.Button(side_frame, text="CHECK LOGS", fg="#ffffff", bg="#31b573", bd=1, pady=5, command=lambda: funcs.check_logs(" "), activebackground="#999999")
currentfundstitle_label = tk.Label(side_frame, text="CURRENT FUNDS", fg="#31ff93", bg="#999999", font=("Bahnschrift", 17))
currentfunds_label = tk.Label(side_frame, text=f"{funcs.check_funds()}", fg="#ffffff", bg="#000000", font=("Bahnschrift", 13), bd=1, border=12,relief=tk.SUNKEN)

title_label.bind("<Button-1>", lambda event: funcs.home(event, main_frame))
title_label.bind("<Enter>", lambda event: funcs.hover(event, title_label))
title_label.bind("<Leave>", lambda event: funcs.unhover(event, title_label))

# side_frame children grid
title_label.grid(row=0, column=0, pady=8)
add_button.grid(row=1, column=0, pady=8, padx=20, sticky="ew")
deduct_button.grid(row=2, column=0, pady=8, padx=20, sticky="ew")
checklog_button.grid(row=3, column=0, pady=8, padx=20, sticky="ew")
currentfundstitle_label.grid(row=4, column=0, pady=8, padx=20, sticky="s")
currentfunds_label.grid(row=5, column=0, pady=(0, 50), padx=20, sticky="sew")

side_frame.columnconfigure(0, weight=1)
side_frame.rowconfigure(4, weight=1)
side_frame.rowconfigure(5, weight=0)

# main_frame children initialization (HOME)
home_label = tk.Label(main_frame, text="Welcome to Money Handler!", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 20), anchor="center")
home_description = tk.Label(main_frame, text="Where tracking your budget and logging down purchases can be made simpler. \nStart by adding your existing funds by pressing the \"ADD FUNDS\" button.", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 13), anchor="center")

# main_frame children grid (HOME)
home_label.grid(row=0, column=0, pady=8, sticky="ew")
home_description.grid(row=1, column=0, pady=8, sticky="ew")

main_frame.columnconfigure(0, weight=1)

# main_frame children initialization (ADD FUNDS)
aftitle_label = tk.Label(main_frame, text="- ADD FUNDS -", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 20))
afamount_label = tk.Label(main_frame, text="Amount:", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 15))
afamount_entry = tk.Entry(main_frame)
afcomment_label = tk.Label(main_frame, text="Comment:", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 15))
afcomment_entry = tk.Entry(main_frame)
af_button = tk.Button(main_frame, text="SUBMIT", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), padx=30, anchor="center", activeforeground="#31b573", activebackground="#ffffff")

# deduct funds fixed comments
COST_OF_LIVING = {1: "Groceries", 2: "Electricity", 3: "Water", 4: "Other Cost of Living"}
PROPERTY_EXPENSES = {1: "Car Upgrades", 2: "Car Repairs", 3: "Car Maintenance", 4: "House Upgrades", 5: "House Repairs", 6: "House Maintenance", 7: "Land", 8: "Other Property Expenses"}
MEDICAL_EXPENSES = {1: "Hospital Fees", 2: "Equipment", 3: "Meds", 4: "Other Medical Fees"}
INSURANCE = {1: "Health Insurance", 2: "Car Insurance", 3: "Other Insurance"}
TAXES = {1: "Taxes"}
INVESTMENTS = {1: "Investments"}
DEBT = {1: "One's Debt", 2: "Someone's Debt"}
MISCELLANEOUS = {1: "Travel Expenses", 2: "Random Buys", 3: "Mug", 4: "Other Miscellaneous"}

# main_frame children initialization (DEDUCT FUNDS)

df_col_button = tk.Button(main_frame, text="Cost of Living", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_pe_button = tk.Button(main_frame, text="Property Expenses", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_me_button = tk.Button(main_frame, text="Medical Expenses", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_is_button = tk.Button(main_frame, text="Insurance", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_t_button = tk.Button(main_frame, text="Taxes", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_iv_button = tk.Button(main_frame, text="Investments", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_d_button = tk.Button(main_frame, text="Debt", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")
df_mi_button = tk.Button(main_frame, text="Miscellaneous", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), anchor="center")

dftitle_label = tk.Label(main_frame, text="- DEDUCT FUNDS -", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 20))
dfamount_label = tk.Label(main_frame, text="Amount:", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 15))
dfamount_entry = tk.Entry(main_frame)
dfcomment_label = tk.Label(main_frame, text="Comment:", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 15))
dfcomment_entry = tk.Entry(main_frame)
df_button = tk.Button(main_frame, text="SUBMIT", fg="#ffffff", bg="#31b573", font=("Bahnschrift", 17), padx=30, anchor="center", activeforeground="#31b573", activebackground="#ffffff")

root.mainloop()
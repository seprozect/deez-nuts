import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import LabelFrame, Label, Button, Entry, Frame, Scrollbar
from PIL import Image, ImageTk
from database import Warehouse
from ttkthemes import themed_tk

if __name__ == '__main__':

    db = Warehouse("warehouse.db")


    def populate_list():
        warehouse_list_listbox.delete(0, tk.END)
        for num, row in enumerate(db.fetch_all_rows()):
            string = ""
            for i in row:
                string = string + "  |  " + str(i)
            string = str(num + 1) + string
            warehouse_list_listbox.insert(tk.END, string)


    # Function to bind listbox
    def select_item(event):
        try:
            global selected_item
            # Use the curselection technique to question the selection. A list of item indexes is returned
            index = warehouse_list_listbox.curselection()[0]
            selected_item = warehouse_list_listbox.get(index)
            selected_item = selected_item.split("  |  ")
            selected_item = db.fetch_by_warehouse_no(selected_item[1])
            clear_input()

            warehouse_no_entry.insert(0, selected_item[0][1])
            warehouse_product_id_entry.insert(0, selected_item[0][2])
            capacity_entry.insert(0, selected_item[0][3])
            location_entry.insert(0, selected_item[0][4])
        except IndexError:
            pass


    # Create main window with using themed_tk
    # provides themed widgets and window styles for Tkinter
    root = themed_tk.ThemedTk()
    root.set_theme("scidpurple")

    root.title("Deez Nuts Inventory Management System")
    width = 1080
    height = 700
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    # get the dimensions of the screen, in pixels. The window is then positioned in the center of the screen by dividing these dimensions by 2 and subtracting half the width and height of the window.
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.columnconfigure(0, weight=1)
    im = Image.open("images//icon.png")
    icon = ImageTk.PhotoImage(im)
    # Set the window icon using the PhotoImage object
    root.wm_iconphoto(True, icon)

    warehouse_frame = LabelFrame(root, text="Enter Warehouse Details")
    # Warehouse No
    warehouse_no_var = tk.StringVar()
    warehouse_no_label = Label(warehouse_frame, text="Warehouse No: ")
    warehouse_no_label.grid(row=0, column=0, sticky="w", padx=10)
    warehouse_no_entry = Entry(warehouse_frame, textvariable=warehouse_no_var)
    warehouse_no_entry.grid(row=0, column=1)

    # Product ID
    warehouse_product_id_var = tk.StringVar()
    warehouse_product_id_label = Label(warehouse_frame, text="Product ID: ")
    warehouse_product_id_label.grid(row=1, column=0, sticky="w", padx=10)
    warehouse_product_id_entry = Entry(warehouse_frame, textvariable=warehouse_product_id_var)
    warehouse_product_id_entry.grid(row=1, column=1)

    # Capacity
    capacity_var = tk.StringVar()
    capacity_label = Label(warehouse_frame, text="Capacity: ")
    capacity_label.grid(row=0, column=2, sticky="w", padx=10)
    capacity_entry = Entry(warehouse_frame, textvariable=capacity_var)
    capacity_entry.grid(row=0, column=3)

    # Location
    location_var = tk.StringVar()
    location_label = Label(warehouse_frame, text="Location: ")
    location_label.grid(row=1, column=2, sticky="w", padx=10)
    location_entry = Entry(warehouse_frame, textvariable=location_var)
    location_entry.grid(row=1, column=3)

    # ****************************************** #

    # Product List
    # frame containing product listing and scrollbar
    listing_frame = Frame(root, borderwidth=1, relief="raised")
    warehouse_list_listbox = tk.Listbox(listing_frame)
    warehouse_list_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="we")
    # binding list box to show selected items in the entry fields.
    warehouse_list_listbox.bind("<<ListboxSelect>>", select_item)

    # Create ScrollBar
    scroll_bar = Scrollbar(listing_frame)
    scroll_bar.config(command=warehouse_list_listbox.yview)
    scroll_bar.grid(row=0, column=1, sticky="ns")

    # Attach Scrollbar to Listbox
    warehouse_list_listbox.config(yscrollcommand=scroll_bar.set)

    # =========================#

    # Create Statusbar using Label widget onto root
    statusbar_label = tk.Label(
        root, text="Status: ", bg="#ffb5c5", anchor="w", font=("arial", 10)
    )
    statusbar_label.grid(row=3, column=0, sticky="we", padx=10)


    # ========================#

    # Button Functions
    def add_item():
        if (
                warehouse_no_var.get() == ""
                or warehouse_product_id_var.get() == ""
                or capacity_var.get() == ""
                or location_var.get() == ""
        ):
            messagebox.showerror(title="Required Fields", message="Please enter all fields")
            return

        db.insert(
            warehouse_no_var.get(),
            warehouse_product_id_var.get(),
            capacity_var.get(),
            location_var.get(),
        )
        clear_input()
        populate_list()
        statusbar_label["text"] = "Status: Product added successfully"
        statusbar_label.config(bg='green', fg='white')


    def update_item():
        if (
                warehouse_no_var.get() != ""
                and warehouse_product_id_var.get() != ""
                and capacity_var.get() != ""
                and location_var.get() != ""):
            db.update(
                selected_item[0][0],
                warehouse_no_var.get(),
                warehouse_product_id_var.get(),
                capacity_var.get(),
                location_var.get(),
            )
            populate_list()
            statusbar_label["text"] = "Status: Product updated successfully"
            statusbar_label.config(bg='green', fg='white')
            return
        messagebox.showerror(title="Required Fields", message="Please enter all fields")
        statusbar_label["text"] = "Please enter all fields"
        statusbar_label.config(bg='red', fg='white')


    def remove_item():
        db.remove(selected_item[0][1])
        clear_input()
        populate_list()
        statusbar_label["text"] = "Status: Product removed from the list successfully"
        statusbar_label.config(bg='green', fg='white')


    def clear_input():
        warehouse_no_entry.delete(0, tk.END)
        warehouse_product_id_entry.delete(0, tk.END)
        capacity_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

    # Buttons
    button_frame = Frame(root, borderwidth=2, relief="groove")

    add_item_btn = Button(button_frame, text="Add item", command=add_item)
    add_item_btn.grid(row=0, column=0, sticky="we", padx=10, pady=5)

    remove_item_btn = Button(button_frame, text="Remove item", command=remove_item)
    remove_item_btn.grid(row=0, column=1, sticky="we", padx=10, pady=5)

    update_item_btn = Button(button_frame, text="Update item", command=update_item)
    update_item_btn.grid(row=0, column=2, sticky="we", padx=10, pady=5)

    clear_item_btn = Button(button_frame, text="Clear Input", command=clear_input)
    clear_item_btn.grid(row=0, column=3, sticky="we", padx=10, pady=5)

    warehouse_frame.grid(row=0, column=0, sticky="we", padx=10, pady=5)
    button_frame.grid(row=1, column=0, sticky="we", padx=10, pady=5)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)
    button_frame.grid_columnconfigure(3, weight=1)
    button_frame.grid_columnconfigure(4, weight=1)
    listing_frame.grid(row=2, column=0, sticky="we", padx=10)
    listing_frame.grid_columnconfigure(0, weight=2)

    populate_list()

    root.mainloop()

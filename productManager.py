import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import LabelFrame, Label, Frame, Scrollbar, Treeview
from tkinter import *
from tkinter.ttk import Progressbar, Entry, Button
from ttkthemes import themed_tk
from database import Products, Warehouse
from PIL import Image, ImageTk

if __name__ == '__main__':

    products_db = Products("products.db")
    warehouse_db = Warehouse("warehouse.db")


    def populate_list():
        product_list_listbox.delete(0, tk.END)
        for num, row in enumerate(products_db.fetch_all_rows()):
            string = ""
            for i in row:
                string = string + "  |  " + str(i)
            string = str(num + 1) + string
            product_list_listbox.insert(tk.END, string)

    def search_warehouse():
        # Get the warehouse ID entered by the user
        search_id = search_warehouse_id_var.get()

        # Clear the existing results
        results_listbox.delete(0, tk.END)

        # Perform the search in the warehouse database
        matching_items = products_db.search_by_warehouse_no(search_id)

        if matching_items:
            # If there are matching items, populate the results_listbox
            for item in matching_items:
                result_string = f"Warehouse ID: {item[0]}, Product ID: {item[1]}, Quantity: {item[2]}"
                results_listbox.insert(tk.END, result_string)
        else:
            # If no matching items are found, display a message
            results_listbox.insert(tk.END, "No matching items found")

    # Function to bind listbox
    def select_item(event):
        try:
            global selected_item
            # Use the curselection technique to question the selection. A list of item indexes is returned
            index = product_list_listbox.curselection()[0]
            selected_item = product_list_listbox.get(index)
            selected_item = selected_item.split("  |  ")
            selected_item = products_db.fetch_by_product_id(selected_item[1])
            clear_input()

            product_id_entry.insert(0, selected_item[0][1])
            warehouse_id_entry.insert(0, selected_item[0][2])
            product_brand_entry.insert(0, selected_item[0][3])
            product_name_entry.insert(0, selected_item[0][4])
            existing_quantity_entry.insert(0, selected_item[0][5])
            cost_price_entry.insert(0, selected_item[0][6])
            selling_price_entry.insert(0, selected_item[0][7])
        except IndexError:
            pass


    # Create main window
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

    entry_frame = LabelFrame(root, text="Enter Product Details")
    # Product ID
    product_id_var = tk.StringVar()
    product_id_label = Label(entry_frame, text="Product ID: ")
    product_id_label.grid(row=0, column=0, sticky="w", padx=10)
    product_id_entry = Entry(entry_frame, textvariable=product_id_var)
    product_id_entry.grid(row=0, column=1)

    # Warehouse ID
    warehouse_id_var = tk.StringVar()
    warehouse_id_label = Label(entry_frame, text="Warehouse ID: ")
    warehouse_id_label.grid(row=1, column=0, sticky="w", padx=10)
    warehouse_id_entry = Entry(entry_frame, textvariable=warehouse_id_var)
    warehouse_id_entry.grid(row=1, column=1)

    # Product Brand
    product_brand_var = tk.StringVar()
    product_brand_label = Label(entry_frame, text="Product Brand: ")
    product_brand_label.grid(row=0, column=2, sticky="w", padx=10)
    product_brand_entry = Entry(entry_frame, textvariable=product_brand_var)
    product_brand_entry.grid(row=0, column=3)

    # Product Name
    product_name_var = tk.StringVar()
    product_name_label = Label(entry_frame, text="Product Name: ")
    product_name_label.grid(row=1, column=2, sticky="w", padx=10)
    product_name_entry = Entry(entry_frame, textvariable=product_name_var)
    product_name_entry.grid(row=1, column=3)

    # Existing Quantity
    existing_quantity_var = tk.StringVar()
    existing_quantity_label = Label(entry_frame, text="Existing Quantity: ")
    existing_quantity_label.grid(row=0, column=4, sticky="w", padx=10)
    existing_quantity_entry = Entry(entry_frame, textvariable=existing_quantity_var)
    existing_quantity_entry.grid(row=0, column=5)

    # Cost Price
    cost_price_var = tk.StringVar()
    cost_price_label = Label(entry_frame, text="Cost Price: ")
    cost_price_label.grid(row=1, column=4, sticky="w", padx=10)
    cost_price_entry = Entry(entry_frame, textvariable=cost_price_var)
    cost_price_entry.grid(row=1, column=5)

    # Selling Price
    selling_price_var = tk.StringVar()
    selling_price_label = Label(entry_frame, text="Selling Price: ")
    selling_price_label.grid(row=2, column=0, sticky="w", padx=10)
    selling_price_entry = Entry(entry_frame, textvariable=selling_price_var)
    selling_price_entry.grid(row=2, column=1)

    # Warehouse Search
    warehouse_frame = LabelFrame(root, text="Warehouse Search")

    # Warehouse ID for search
    search_warehouse_id_var = tk.StringVar()
    search_warehouse_id_label = Label(warehouse_frame, text="Enter Warehouse ID:")
    search_warehouse_id_label.grid(row=0, column=0, sticky="w", columnspan=2, padx=15)
    search_warehouse_id_entry = Entry(warehouse_frame, textvariable=search_warehouse_id_var)
    search_warehouse_id_entry.grid(row=0, column=3,columnspan=4, padx=15)

    # Search Button
    search_button = Button(warehouse_frame, text="Search", command=search_warehouse)
    search_button.grid(row=0, column=10, columnspan=2, padx=20)

    # Listbox for Warehouse results
    results_frame = Frame(root, borderwidth=1, relief="raised")
    results_listbox = tk.Listbox(results_frame)
    results_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="we")

    # Scrollbar for the listbox
    scrollbar = Scrollbar(results_frame)
    scrollbar.grid(row=0, column=1, sticky="ns")
    results_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=results_listbox.yview)


    # ****************************************** #

    # Product List
    # frame containing product listing and scrollbar
    listing_frame = Frame(root, borderwidth=1, relief="raised")
    product_list_listbox = tk.Listbox(listing_frame)
    product_list_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="we")
    # binding list box to show selected items in the entry fields.
    product_list_listbox.bind("<<ListboxSelect>>", select_item)

    # Create ScrollBar
    scroll_bar = Scrollbar(listing_frame)
    scroll_bar.config(command=product_list_listbox.yview)
    scroll_bar.grid(row=0, column=1, sticky="ns")

    # Attach Scrollbar to Listbox
    product_list_listbox.config(yscrollcommand=scroll_bar.set)

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
                product_id_var.get() == ""
                or warehouse_id_var.get() == ""
                or product_brand_var.get() == ""
                or product_name_var.get() == ""
                or existing_quantity_var.get() == ""
                or cost_price_var.get() == ""
                or selling_price_var.get() == ""
        ):
            messagebox.showerror(title="Required Fields", message="Please enter all fields")
            return

        products_db.insert(
            product_id_var.get(),
            warehouse_id_var.get(),
            product_brand_var.get(),
            product_name_var.get(),
            existing_quantity_var.get(),
            cost_price_var.get(),
            selling_price_var.get(),
        )
        clear_input()
        populate_list()
        statusbar_label["text"] = "Status: Product added successfully"
        statusbar_label.config(bg='green', fg='white')


    def update_item():
        if (
                product_id_var.get() != ""
                and warehouse_id_var.get() != ""
                and product_brand_var.get() != ""
                and product_name_var.get() != ""
                and existing_quantity_var.get() != ""
                and cost_price_var.get() != ""
                and selling_price_var.get() != ""):
            products_db.update(
                selected_item[0][0],
                product_id_var.get(),
                warehouse_id_var.get(),
                product_brand_var.get(),
                product_name_var.get(),
                existing_quantity_var.get(),
                cost_price_var.get(),
                selling_price_var.get(),
            )
            populate_list()
            statusbar_label["text"] = "Status: Product updated successfully"
            statusbar_label.config(bg='green', fg='white')
            return
        messagebox.showerror(title="Required Fields", message="Please enter all fields")
        statusbar_label["text"] = "Please enter all fields"
        statusbar_label.config(bg='red', fg='white')


    def remove_item():
        products_db.remove(selected_item[0][1])
        clear_input()
        populate_list()
        statusbar_label["text"] = "Status: Product removed from the list successfully"
        statusbar_label.config(bg='green', fg='white')


    def clear_input():
        product_id_entry.delete(0, tk.END)
        warehouse_id_entry.delete(0, tk.END)
        product_brand_entry.delete(0, tk.END)
        product_name_entry.delete(0, tk.END)
        existing_quantity_entry.delete(0, tk.END)
        cost_price_entry.delete(0, tk.END)
        selling_price_entry.delete(0, tk.END)

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

    entry_frame.grid(row=0, column=0, sticky="we", padx=10, pady=5)
    warehouse_frame.grid(row=4, column=0, sticky="we", padx=10, pady=15)
    button_frame.grid(row=1, column=0, sticky="we", padx=10, pady=5)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)
    button_frame.grid_columnconfigure(3, weight=1)
    button_frame.grid_columnconfigure(4, weight=1)
    listing_frame.grid(row=2, column=0, sticky="we", padx=10)
    listing_frame.grid_columnconfigure(0, weight=2)
    results_frame.grid(row=5, column=0, sticky="we", padx=10)
    results_frame.grid_columnconfigure(0, weight=2)

    populate_list()
# ---------------------------------------------------- Second Page -----------------------------------------------------------------------------

    def open_dashboard():
        dashboard_window = tk.Toplevel(root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry('800x400')
        dashboard_window.iconphoto(True, icon)

        # Dashboard Title
        dashboard_title = Label(dashboard_window, text="Inventory Management Dashboard", font=("Arial", 16))
        dashboard_title.pack(pady=10)

        # Display Metrics
        metrics_frame = LabelFrame(dashboard_window, text="Key Metrics")
        metrics_frame.pack(padx=20, pady=10, fill='both', expand=True)

        total_products_label = Label(metrics_frame, text="Total Products:")
        total_products_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        total_products_value = Label(metrics_frame, text=len(products_db.fetch_all_rows()))
        total_products_value.grid(row=0, column=1, padx=10, pady=5)

        total_stock_value_label = Label(metrics_frame, text="Total Stock Value:")
        total_stock_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        total_stock_value = Label(metrics_frame, text="Calculate Total Stock Value Here")  # You can compute this value
        total_stock_value.grid(row=1, column=1, padx=10, pady=5)

        # Recent Transactions
        transactions_frame = LabelFrame(dashboard_window, text="Recent Transactions")
        transactions_frame.pack(padx=20, pady=10, fill='both', expand=True)

        transactions_treeview = Treeview(transactions_frame, columns=("Date", "Transaction Type", "Product Name"),
                                         show="headings")
        transactions_treeview.heading("Date", text="Date")
        transactions_treeview.heading("Transaction Type", text="Transaction Type")
        transactions_treeview.heading("Product Name", text="Product Name")

        transactions_treeview.column("Date", width=150)
        transactions_treeview.column("Transaction Type", width=150)
        transactions_treeview.column("Product Name", width=250)

        transactions_treeview.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        scrollbar = Scrollbar(transactions_frame, orient="vertical", command=transactions_treeview.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        transactions_treeview.configure(yscrollcommand=scrollbar.set)

        # Add sample transactions (replace with actual data)
        transactions_treeview.insert("", "end", values=("2023-10-01", "Purchase", "Product A"))
        transactions_treeview.insert("", "end", values=("2023-10-02", "Sale", "Product B"))
        transactions_treeview.insert("", "end", values=("2023-10-03", "Sale", "Product C"))


    # Add a "Dashboard" button to the main window
    dashboard_button = Button(root, text="Open Dashboard", command=open_dashboard)
    dashboard_button.grid(row=6, column=0, sticky="we", padx=10, pady=5)

    print(1)
    root.mainloop()
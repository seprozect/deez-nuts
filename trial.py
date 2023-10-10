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
    total_stock_value = Label(metrics_frame, text="$250145")  # You can compute this value
    total_stock_value.grid(row=1, column=1, padx=10, pady=5)

    # Product Search
    product_frame = LabelFrame(dashboard_window, text="Warehouse Search")
    # Warehouse ID for search
    search_product_name_var = tk.StringVar()
    search_product_name_label = Label(warehouse_frame, text="Enter Warehouse ID:")
    search_product_name_label.grid(row=0, column=0, sticky="w", columnspan=2, padx=15)
    search_product_name_entry = Entry(warehouse_frame, textvariable=search_product_name_var)
    search_product_name_entry.grid(row=0, column=3, columnspan=4, padx=15)

    # Search Button
    search_button = Button(product_frame, text="Search", command=search_warehouse)
    search_button.grid(row=10, column=10, columnspan=2, padx=20)

    # Listbox for Warehouse results
    results_frame = Frame(dashboard_window, borderwidth=1, relief="raised")
    results_listbox = tk.Listbox(results_frame)
    results_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="we")

    # Scrollbar for the listbox
    scrollbar = Scrollbar(results_frame)
    scrollbar.grid(row=0, column=1, sticky="ns")
    results_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=results_listbox.yview)
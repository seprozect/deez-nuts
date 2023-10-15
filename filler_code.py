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
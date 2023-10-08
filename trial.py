def open_blank_window():
    new_window = tk.Toplevel(root)
    new_window.title("Blank Window")
    new_window.geometry("400x300")
    # You can add widgets and customize this blank window as needed.


# Create a button to open the blank window
open_window_btn = Button(root, text="Open Blank Window", command=open_blank_window)
open_window_btn.grid(row=6, column=0, sticky="we", padx=10, pady=10)






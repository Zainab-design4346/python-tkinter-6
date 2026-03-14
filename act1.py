import tkinter as tk
from tkinter import ttk, messagebox

class Restro:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Management")
        self.menu_items = {
            "BURGER": 10,
            "PIZZA": 20,
            "DRINKS": 5
        }
        bg_width, bg_height = 800, 600 
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Pizza Express Restaurant", font=("Arial", 20, "bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame,text=f"{item} (Aed.{price}):")
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        order_button = ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,columnspan=3,padx=10,pady=10)
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        symbol = "aed"
        for item, entry in self.menu_quantities.items():
            quantity = int(entry.get())
            price = self.menu_items[item]
            cost = quantity * price
            total_cost += cost
            order_summary  += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        order_summary += f"\nTotal Cost: {symbol}{total_cost}"
        messagebox.showinfo("Order placed", order_summary)

if __name__== "__main__":
    root = tk.Tk()
    app = Restro(root)
    root.geometry("800x600")
    root.mainloop()
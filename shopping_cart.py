import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        self.root.geometry("800x600")
        self.root.configure(bg="#e8f4fd")
        
        # Initialize cart
        self.cart = []
        self.current_item = {"food": "", "price": 0.0}
        
        # Configure style
        self.setup_styles()
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#e8f4fd")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        self.create_header()
        
        # Create input section
        self.create_input_section()
        
        # Create cart display
        self.create_cart_display()
        
        # Create buttons
        self.create_buttons()
        
        # Bind Enter key
        self.root.bind('<Return>', lambda event: self.process_input())
        
        # Bind Delete key for removing items
        self.root.bind('<Delete>', lambda event: self.remove_selected_item())
        
        # Focus on food entry
        self.food_entry.focus()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#f0f0f0')
        style.configure('Info.TLabel', font=('Arial', 10), background='#f0f0f0')
        style.configure('Cart.TLabel', font=('Arial', 9), background='#ffffff')
        
        style.configure('Add.TButton', font=('Arial', 10, 'bold'))
        style.configure('Clear.TButton', font=('Arial', 10))
        style.configure('Checkout.TButton', font=('Arial', 12, 'bold'))

    def create_header(self):
        header_frame = tk.Frame(self.main_frame, bg="#e8f4fd")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(header_frame, text="🛒 Shopping Cart", 
                              font=("Arial", 20, "bold"), bg="#e8f4fd", fg="#1e3a8a")
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame, text="Enter your items and prices", 
                                 font=("Arial", 12), bg="#e8f4fd", fg="#475569")
        subtitle_label.pack()
        
        # Instructions
        instructions_label = tk.Label(header_frame, 
                                    text="💡 Tip: Press Enter to add items, Delete to remove selected item, or type 'q' to generate receipt", 
                                    font=("Arial", 10), bg="#e8f4fd", fg="#dc2626")
        instructions_label.pack(pady=(5, 0))

    def create_input_section(self):
        input_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.RAISED, bd=2)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Food input
        food_frame = tk.Frame(input_frame, bg="#ffffff")
        food_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.food_label = tk.Label(food_frame, text="Enter Food to Buy (press 'q' to quit):", 
                                  font=("Arial", 12, "bold"), bg="#ffffff", fg="#1e3a8a")
        self.food_label.pack(anchor=tk.W)
        
        self.food_entry = tk.Entry(food_frame, font=("Arial", 12), width=40, 
                                  relief=tk.SOLID, bd=2, bg="#f8fafc")
        self.food_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Price input (always visible)
        price_frame = tk.Frame(input_frame, bg="#ffffff")
        price_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.price_label = tk.Label(price_frame, text="Enter Price of Food:", 
                                   font=("Arial", 12, "bold"), bg="#ffffff", fg="#1e3a8a")
        self.price_label.pack(anchor=tk.W)
        
        self.price_entry = tk.Entry(price_frame, font=("Arial", 12), width=40, 
                                   relief=tk.SOLID, bd=2, bg="#f8fafc")
        self.price_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Quantity input (always visible)
        quantity_frame = tk.Frame(input_frame, bg="#ffffff")
        quantity_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.quantity_label = tk.Label(quantity_frame, text="Enter Quantity:", 
                                      font=("Arial", 12, "bold"), bg="#ffffff", fg="#1e3a8a")
        self.quantity_label.pack(anchor=tk.W)
        
        self.quantity_entry = tk.Entry(quantity_frame, font=("Arial", 12), width=40, 
                                      relief=tk.SOLID, bd=2, bg="#f8fafc")
        self.quantity_entry.pack(fill=tk.X, pady=(5, 0))
        self.quantity_entry.insert(0, "1")  # Default quantity is 1

    def create_cart_display(self):
        cart_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.RAISED, bd=2)
        cart_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        cart_header = tk.Label(cart_frame, text="🛍️ Your Shopping Cart", 
                              font=("Arial", 14, "bold"), bg="#ffffff", fg="#1e3a8a")
        cart_header.pack(pady=10)
        
        # Create Treeview for cart items
        self.cart_tree = ttk.Treeview(cart_frame, columns=("Item", "Price", "Quantity", "Total"), show="headings", height=8)
        self.cart_tree.heading("Item", text="Item")
        self.cart_tree.heading("Price", text="Price ($)")
        self.cart_tree.heading("Quantity", text="Qty")
        self.cart_tree.heading("Total", text="Total ($)")
        self.cart_tree.column("Item", width=200, anchor=tk.W)
        self.cart_tree.column("Price", width=80, anchor=tk.E)
        self.cart_tree.column("Quantity", width=60, anchor=tk.CENTER)
        self.cart_tree.column("Total", width=80, anchor=tk.E)
        self.cart_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 10))
        
        # Cart action buttons
        cart_buttons_frame = tk.Frame(cart_frame, bg="#ffffff")
        cart_buttons_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        # Remove selected item button
        self.remove_button = ttk.Button(cart_buttons_frame, text="Remove Selected", 
                                       command=self.remove_selected_item, style='Clear.TButton')
        self.remove_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Total label
        self.total_label = tk.Label(cart_frame, text="Total: $0.00", 
                                   font=("Arial", 14, "bold"), bg="#ffffff", fg="#059669")
        self.total_label.pack(pady=10)

    def create_buttons(self):
        button_frame = tk.Frame(self.main_frame, bg="#e8f4fd")
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Add button
        self.add_button = ttk.Button(button_frame, text="Add to Cart", 
                                    command=self.add_to_cart, style='Add.TButton')
        self.add_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_button = ttk.Button(button_frame, text="Clear Cart", 
                                      command=self.clear_cart, style='Clear.TButton')
        self.clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Checkout button
        self.checkout_button = ttk.Button(button_frame, text="Generate Receipt", 
                                         command=self.generate_receipt, style='Checkout.TButton')
        self.checkout_button.pack(side=tk.RIGHT)

    def process_input(self):
        # Get food input
        food = self.food_entry.get().strip()
        
        if not food:
            messagebox.showwarning("Warning", "Please enter a food item!")
            return
            
        if food.lower() == 'q':
            self.generate_receipt()
            return
            
        # Try to add to cart
        self.add_to_cart()

    def add_to_cart(self):
        # Get food, price, and quantity inputs
        food = self.food_entry.get().strip()
        price_text = self.price_entry.get().strip()
        quantity_text = self.quantity_entry.get().strip()
        
        if not food:
            messagebox.showwarning("Warning", "Please enter a food item!")
            return
            
        if not price_text:
            messagebox.showwarning("Warning", "Please enter a price!")
            return
            
        if not quantity_text:
            messagebox.showwarning("Warning", "Please enter a quantity!")
            return
            
        try:
            price = float(price_text)
            quantity = int(quantity_text)
            
            if price < 0:
                raise ValueError("Price cannot be negative")
                
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")
                
            # Add to cart with quantity
            self.cart.append((food, price, quantity))
            
            # Update cart display
            self.update_cart_display()
            
            # Clear inputs and reset
            self.food_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, "1")  # Reset to default
            self.food_entry.focus()
            
            # Silent success - no message box when adding items
            
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid price and quantity!")

    def update_cart_display(self):
        # Clear existing items
        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)
        
        # Add items to treeview
        for food, price, quantity in self.cart:
            item_total = price * quantity
            self.cart_tree.insert("", tk.END, values=(food, f"${price:.2f}", quantity, f"${item_total:.2f}"))
        
        # Update total
        total = sum(item[1] * item[2] for item in self.cart)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def remove_selected_item(self):
        selected_item = self.cart_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to remove!")
            return
            
        # Get the index of selected item
        item_index = self.cart_tree.index(selected_item[0])
        
        # Remove from cart
        removed_item = self.cart.pop(item_index)
        
        # Update display
        self.update_cart_display()
        
        messagebox.showinfo("Removed", f"Removed {removed_item[0]} (Qty: {removed_item[2]}) from cart!")

    def clear_cart(self):
        if messagebox.askyesno("Clear Cart", "Are you sure you want to clear the cart?"):
            self.cart.clear()
            self.update_cart_display()
            self.food_entry.focus()

    def generate_receipt(self):
        if not self.cart:
            messagebox.showinfo("Empty Cart", "Your cart is empty!")
            return
        
        # Create receipt window
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")
        receipt_window.geometry("500x600")
        receipt_window.configure(bg="#ffffff")
        
        # Receipt content
        receipt_frame = tk.Frame(receipt_window, bg="#ffffff")
        receipt_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_label = tk.Label(receipt_frame, text="🛒 SHOPPING RECEIPT", 
                               font=("Arial", 18, "bold"), bg="#ffffff", fg="#1e3a8a")
        header_label.pack(pady=(0, 10))
        
        # Date and time
        now = datetime.datetime.now()
        date_label = tk.Label(receipt_frame, text=f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}", 
                             font=("Arial", 10), bg="#ffffff", fg="#475569")
        date_label.pack(pady=(0, 20))
        
        # Items
        items_frame = tk.Frame(receipt_frame, bg="#ffffff")
        items_frame.pack(fill=tk.BOTH, expand=True)
        
        # Headers
        headers_frame = tk.Frame(items_frame, bg="#ffffff")
        headers_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Configure grid columns for proper alignment
        headers_frame.grid_columnconfigure(0, weight=1)
        headers_frame.grid_columnconfigure(1, weight=0)
        headers_frame.grid_columnconfigure(2, weight=0)
        headers_frame.grid_columnconfigure(3, weight=0)
        
        # Create a grid for better alignment
        tk.Label(headers_frame, text="Item", font=("Arial", 12, "bold"), 
                bg="#ffffff", fg="#1e3a8a", width=20, anchor=tk.W).grid(row=0, column=0, sticky=tk.W)
        tk.Label(headers_frame, text="Price", font=("Arial", 12, "bold"), 
                bg="#ffffff", fg="#1e3a8a", width=10, anchor=tk.CENTER).grid(row=0, column=1, padx=10)
        tk.Label(headers_frame, text="Qty", font=("Arial", 12, "bold"), 
                bg="#ffffff", fg="#1e3a8a", width=8, anchor=tk.CENTER).grid(row=0, column=2, padx=10)
        tk.Label(headers_frame, text="Total", font=("Arial", 12, "bold"), 
                bg="#ffffff", fg="#1e3a8a", width=12, anchor=tk.E).grid(row=0, column=3, sticky=tk.E)
        
        # Separator
        separator = tk.Frame(items_frame, height=2, bg="#bdc3c7")
        separator.pack(fill=tk.X, pady=(0, 10))
        
        # Items list
        for i, (food, price, quantity) in enumerate(self.cart):
            item_frame = tk.Frame(items_frame, bg="#ffffff")
            item_frame.pack(fill=tk.X, pady=2)
            
            # Configure grid columns for proper alignment
            item_frame.grid_columnconfigure(0, weight=1)
            item_frame.grid_columnconfigure(1, weight=0)
            item_frame.grid_columnconfigure(2, weight=0)
            item_frame.grid_columnconfigure(3, weight=0)
            
            item_total = price * quantity
            
            # Create a grid for better alignment
            tk.Label(item_frame, text=food, font=("Arial", 11), 
                    bg="#ffffff", fg="#1e3a8a", width=20, anchor=tk.W).grid(row=0, column=0, sticky=tk.W)
            tk.Label(item_frame, text=f"${price:.2f}", font=("Arial", 11), 
                    bg="#ffffff", fg="#1e3a8a", width=10, anchor=tk.CENTER).grid(row=0, column=1, padx=10)
            tk.Label(item_frame, text=str(quantity), font=("Arial", 11), 
                    bg="#ffffff", fg="#1e3a8a", width=8, anchor=tk.CENTER).grid(row=0, column=2, padx=10)
            tk.Label(item_frame, text=f"${item_total:.2f}", font=("Arial", 11), 
                    bg="#ffffff", fg="#1e3a8a", width=12, anchor=tk.E).grid(row=0, column=3, sticky=tk.E)
        
        # Total separator
        total_separator = tk.Frame(items_frame, height=2, bg="#bdc3c7")
        total_separator.pack(fill=tk.X, pady=10)
        
        # Total
        total = sum(item[1] * item[2] for item in self.cart)
        total_frame = tk.Frame(items_frame, bg="#ffffff")
        total_frame.pack(fill=tk.X)
        
        # Configure grid columns for proper alignment
        total_frame.grid_columnconfigure(0, weight=1)
        total_frame.grid_columnconfigure(1, weight=0)
        total_frame.grid_columnconfigure(2, weight=0)
        total_frame.grid_columnconfigure(3, weight=0)
        
        # Create a grid for better alignment of total
        tk.Label(total_frame, text="TOTAL:", font=("Arial", 14, "bold"), 
                bg="#ffffff", fg="#1e3a8a", width=20, anchor=tk.W).grid(row=0, column=0, sticky=tk.W)
        tk.Label(total_frame, text="", width=10).grid(row=0, column=1)  # Empty space
        tk.Label(total_frame, text="", width=8).grid(row=0, column=2)   # Empty space
        tk.Label(total_frame, text=f"${total:.2f}", font=("Arial", 14, "bold"), 
                bg="#ffffff", fg="#059669", width=12, anchor=tk.E).grid(row=0, column=3, sticky=tk.E)
        
        # Thank you message
        thank_label = tk.Label(receipt_frame, text="Thank you for your purchase! 🎉", 
                              font=("Arial", 12), bg="#ffffff", fg="#059669")
        thank_label.pack(pady=20)
        
        # Close button
        close_button = ttk.Button(receipt_frame, text="Close Receipt", 
                                 command=receipt_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        self.cart = []

        # Food Entry
        tk.Label(root, text="Enter Food to Buy (q to quit):").pack(pady=5)
        self.food_entry = tk.Entry(root)
        self.food_entry.pack(pady=5)

        # Price Entry
        tk.Label(root, text="Enter Price:").pack(pady=5)
        self.price_entry = tk.Entry(root)
        self.price_entry.pack(pady=5)

        # Add Button
        tk.Button(root, text="Add to Cart", command=self.add_to_cart).pack(pady=5)

        # Cart Display
        self.cart_label = tk.Label(root, text="Your Cart:\nTotal: $0.00")
        self.cart_label.pack(pady=10)

    def add_to_cart(self):
        food = self.food_entry.get().strip()
        if food.lower() == 'q':
            self.show_cart()
            return

        try:
            price = float(self.price_entry.get())
            if price < 0:
                raise ValueError
            self.cart.append((food, price))
            self.food_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added {food} at ${price} to cart.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price.")

    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart", "Cart is empty!")
            return

        total = sum(item[1] for item in self.cart)
        cart_text = "Your Cart:\n" + "\n".join(f"{item[0]}: ${item[1]}" for item in self.cart) + f"\nTotal: ${total:.2f}"
        self.cart_label.config(text=cart_text)
        self.food_entry.config(state='disabled')
        self.price_entry.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()

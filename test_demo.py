#!/usr/bin/env python3
"""
Shopping Cart Demo - Test Script
This script demonstrates the enhanced shopping cart functionality
"""

import tkinter as tk
from shopping_cart import ShoppingCartApp

def main():
    print("🛒 Shopping Cart Demo")
    print("=" * 40)
    print("Features:")
    print("1. Add multiple items (food name + price)")
    print("2. Remove items from cart (select + Delete key or Remove button)")
    print("3. Clear entire cart")
    print("4. Generate receipt when done")
    print("5. Keyboard shortcuts: Enter to add, Delete to remove, 'q' to quit")
    print("=" * 40)
    
    # Launch the application
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
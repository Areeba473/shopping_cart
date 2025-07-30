# 🛒 Shopping Cart Application

A modern, user-friendly shopping cart application built with Python and Tkinter. Features a beautiful GUI with quantity support, item management, and professional receipt generation.

## ✨ Features

### 🎯 Core Functionality
- **Add Items**: Enter food name, price, and quantity
- **Remove Items**: Select and remove individual items from cart
- **Clear Cart**: Remove all items at once
- **Generate Receipt**: Professional receipt with date/time stamp
- **Real-time Total**: Automatic calculation of cart total

### 🎨 User Interface
- **Modern Design**: Clean, colorful interface with light blue theme
- **Responsive Layout**: Well-organized sections for input and display
- **Professional Receipt**: Aligned columns with proper spacing
- **Keyboard Shortcuts**: Enter to add, Delete to remove, 'q' to quit

### 📊 Cart Management
- **Item Details**: Name, price per unit, quantity, and item total
- **Quantity Support**: Specify how many of each item you want
- **Visual Display**: Treeview with organized columns
- **Total Calculation**: Automatic grand total calculation

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python)

### Setup
1. **Clone or Download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd shopping_cart
   ```
3. **Run** the application:
   ```bash
   python shopping_cart.py
   ```

## 📖 How to Use

### Adding Items
1. **Enter Food Name**: Type the name of the item you want to buy
2. **Enter Price**: Specify the price per unit (e.g., $2.50)
3. **Enter Quantity**: How many of this item you want (default: 1)
4. **Press Enter** or click "Add to Cart"
5. **Repeat** for more items

### Managing Cart
- **Remove Item**: Select an item in the cart and press Delete key or click "Remove Selected"
- **Clear All**: Click "Clear Cart" to remove everything
- **View Total**: See the running total at the bottom of the cart

### Generating Receipt
- **Type 'q'** in the food name field to generate a receipt
- **Or click** "Generate Receipt" button anytime
- **Receipt includes**: Date/time, all items with quantities, and total

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Enter** | Add item to cart |
| **Delete** | Remove selected item |
| **'q'** | Generate receipt and quit |

## 🎨 Interface Design

### Color Scheme
- **Background**: Light blue (`#e8f4fd`)
- **Headers**: Dark blue (`#1e3a8a`)
- **Text**: Gray (`#475569`)
- **Totals**: Green (`#059669`)
- **Input Fields**: Light gray (`#f8fafc`)

### Layout Sections
1. **Header**: Title and instructions
2. **Input Section**: Food name, price, and quantity fields
3. **Cart Display**: Organized table with item details
4. **Action Buttons**: Add, remove, clear, and generate receipt

## 📋 Receipt Features

### Professional Layout
- **Date/Time Stamp**: Current date and time
- **Aligned Columns**: Item, Price, Quantity, Total
- **Item Totals**: Price × Quantity for each item
- **Grand Total**: Sum of all item totals
- **Thank You Message**: Professional closing

### Example Receipt
```
🛒 SHOPPING RECEIPT
Date: 2025-07-30 10:37:50

Item                 Price     Qty    Total
Bread               $10.00      1    $10.00
Cake                $20.00      1    $20.00
Coke                $80.00      2   $160.00
Eggs                $30.00      5   $150.00

TOTAL:                                    $340.00

Thank you for your purchase! 🎉
```

## 🔧 Technical Details

### File Structure
```
shopping_cart/
├── shopping_cart.py    # Main application
├── test_demo.py        # Demo script
└── README.md          # This file
```

### Dependencies
- **tkinter**: GUI framework (built-in with Python)
- **datetime**: Date/time functionality (built-in)

### Class Structure
- **ShoppingCartApp**: Main application class
- **Methods**:
  - `add_to_cart()`: Add items with validation
  - `remove_selected_item()`: Remove individual items
  - `clear_cart()`: Remove all items
  - `generate_receipt()`: Create professional receipt
  - `update_cart_display()`: Refresh cart view

## 🐛 Troubleshooting

### Common Issues
1. **Tkinter not found**: Install Python with Tkinter support
2. **Permission errors**: Run with appropriate permissions
3. **Display issues**: Ensure your system supports the color scheme

### Error Messages
- **"Please enter a food item!"**: Food name is required
- **"Please enter a price!"**: Price is required
- **"Please enter a quantity!"**: Quantity is required
- **"Please enter valid price and quantity!"**: Invalid numeric values

## 🎯 Use Cases

### Personal Shopping
- Track grocery items and prices
- Calculate total before checkout
- Generate receipts for records

### Small Business
- Simple point-of-sale system
- Item management with quantities
- Professional receipt generation

### Learning/Education
- Python GUI development
- Tkinter framework usage
- Shopping cart logic implementation

## 🤝 Contributing

Feel free to enhance the application with:
- Additional payment methods
- Item categories
- Discount calculations
- Data persistence
- Export functionality



**Enjoy your shopping experience! 🛍️**

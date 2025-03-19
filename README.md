# Grocery Store App


## Overview
This project provides a simple order management system using Python and MySQL. It allows users to insert new orders, retrieve order details, and fetch all orders stored in the database.

## Features
- Insert new orders with customer details and order items
- Fetch all orders along with their respective details
- Retrieve details of a specific order

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.x
- MySQL database
- Required Python packages (listed in `requirements.txt` if available)

## Database Setup
1. Create a MySQL database and tables using the following schema:

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    datetime DATETIME NOT NULL
);

CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price_per_unit DECIMAL(10,2) NOT NULL
);
```

2. Update `sql_connection.py` to provide a function `get_sql_connection()` that connects to your MySQL database.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/order-management.git
   cd order-management
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script to fetch all orders:
   ```bash
   python orders.py
   ```
2. Modify the script to insert new orders by calling `insert_order()`.

## Functions
### `insert_order(connection, order)`
- Inserts a new order into the database.
- Parameters:
  - `connection`: MySQL connection object.
  - `order`: Dictionary containing customer details and order items.
- Returns:
  - `order_id` of the newly created order.

### `get_order_details(connection, order_id)`
- Retrieves the details of a specific order.
- Parameters:
  - `connection`: MySQL connection object.
  - `order_id`: ID of the order to retrieve.
- Returns:
  - List of order details, including product name and quantity.

### `get_all_orders(connection)`
- Fetches all orders along with their details.
- Parameters:
  - `connection`: MySQL connection object.
- Returns:
  - List of all orders with respective details.

## Example
```python
connection = get_sql_connection()
order = {
    'customer_name': 'John Doe',
    'grand_total': 150.00,
    'order_details': [
        {'product_id': 1, 'quantity': 2, 'total_price': 50.00},
        {'product_id': 3, 'quantity': 1, 'total_price': 30.00}
    ]
}
order_id = insert_order(connection, order)
print(f'Order ID: {order_id}')
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Author
[Mrunal Patange](https://github.com/your-github-profile)


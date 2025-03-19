import mysql.connector

def get_all_products():
    try:
        # Connect to MySQL database
        cnx = mysql.connector.connect(
            user="root",
            password="password",
            host="localhost",
            database="grocery_store"
        )
        cursor = cnx.cursor()

        # Corrected query string with proper spacing
        query = ("""
            SELECT products.product_id, products.name, products.uom_id, 
                   products.price_per_unit, uom.uom_name
            FROM products 
            INNER JOIN uom ON products.uom_id = uom.uom_id
        """)

        # Execute query
        cursor.execute(query)

        # Fetch all results
        results = cursor.fetchall()

        response = []
        for product_id, name, uom_id, price_per_unit, uom_name in results:
            response.append({
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            })

        return response

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    
    finally:
        # Ensure resources are closed
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

# Run the function
if __name__ == '__main__':
    print(get_all_products())

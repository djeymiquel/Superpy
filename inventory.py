from date_time import *
from csv_parser import *
from my_lib2 import *





# Inventory Now 
def inventory_now():
    # Create a "Rich" table with columns for the product name, count, buy price, and expiration date
    table = Table(title="Current Inventory", show_header=True, header_style="green")
    table.add_column("Product Name", style="orange3")
    table.add_column("Count", style="orange3")
    table.add_column("Buy Price", style="orange3")
    table.add_column("Expiration Date", style="orange3")

    # Add a row to the table with the values from the current row of the CSV file
    for row in current_inventory:
        table.add_row(row["Product Name".title()], row["Count"], row["Buy Price"], row["Expiration Date"],end_section=True)
    console.print(table)

 
    
# Inventory Yesterday
def inventory_yesterday():
# Read in the bought.csv file 
# Create a dictionary of all items bought yesterday
    bought_items = {}
    for row in bought_data:
        if row["buy_date"] <= yesterday.strftime("%Y-%m-%d"):
            product_name = row["product_name"]
            buy_price = row["buy_price"]
            if product_name and buy_price:
                count = bought_items.get(product_name,{"Count": 0})["Count"]
                bought_items[product_name] = {
                    "Product Name": row["product_name"],
                    "Count": str(int(count) + 1),
                    "Buy Price": row["buy_price"],
                    "Expiration Date": row["expiration_date"]} 
            # Create the "Rich" table and add the header
    table = Table(title="Yesterday's Inventory", show_header=True, header_style="bold green")
    table.add_column("Product Name", style="orange3")
    table.add_column("Count", style="orange3")
    table.add_column("Buy Price", style="orange3")
    table.add_column("Expiration Date", style="orange3")
    # Add the data to the table
    for item in bought_items.values():
        table.add_row(item["Product Name"], item["Count"], item["Buy Price"], item["Expiration Date"],end_section=True)
    console.print(table)

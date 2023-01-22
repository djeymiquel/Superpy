from my_lib2 import *

def available_store_products():
    table = Table(title="Available Products", show_header=True, header_style="bold green")
    table.add_column("Store Items", style="orange3")
    for product in available_products:
        table.add_row(product['store_items'].title(), end_section=False)
    print(table)


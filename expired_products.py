from my_lib2 import *

def expired():
    table = Table(title="Expired Products", show_header=True, header_style="bold red")
    table.add_column("Exp ID", style="orange3")
    table.add_column("Product Name", style="orange3")
    table.add_column("Buy Date", style="orange3")
    table.add_column("Expiry Date", style="red")
    
    for row in expired_dates:
        table.add_row(row["Exp ID"], row["Product Name".title()], row["Buy Date"], row["Expiry Date"], end_section=True)
    console.print(table)
    

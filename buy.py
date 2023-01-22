from my_lib2 import *
from visual_inventory import *
import pdb

# Buy Products
def buy_product(product_name: str, buy_price: float, expiration_date):
    exp_date = my_date.exp_date(expiration_date)
    
    # Check if product is in Available Items CSV 
    # If True then add product to bought.csv 
    # If False raise an Error message
    # breakpoint()
    try:
        if product_name not in (row["store_items"] for row in available_products):
            raise ValueError(f"ValueError: {product_name.title()} not found in available items")
    
        # Add product to Bought CSV #
        # If row header is empty (position == 0) writeheader
        # append a new product with a unique ID
        with open("files/bought.csv", "a", newline="") as out:
            writer = csv.writer(out)
            position = out.tell()
            if position == 0: # if bought.csv is empty then write header row
                writer.writerow(["ID","product_name","buy_date","buy_price","expiration_date"])         
            writer.writerow(
                [len(list(csv.reader(open("files/bought.csv")))), product_name,today,buy_price,exp_date])
            console.print("OK", style="bold green") 
                
            # Update inventory list #
            # Check if item already exist in the inventory.csv
            # If True count + 1  
            count = 1
            inventory_items = {row["Product Name"]: row for row in current_inventory} # Product name becomes key for inner dictionary
            if product_name in inventory_items:
                inventory_items[product_name]["Count"] = str(int(inventory_items[product_name]["Count"]) + count)
                
            # If not create a new entry with the product name as a entry 
            # key for the inner dictionary
            else:
                inventory_items[product_name] = {"Product Name": product_name,"Count": count,"Buy Price": buy_price,"Expiration Date": exp_date}  
                                            
            # Write the updated inventory list 
            with open("files/inventory.csv", "w") as out:
                fieldnames = ["Product Name","Count","Buy Price","Expiration Date"]
                writer = csv.DictWriter(out, fieldnames=fieldnames)
                writer.writeheader()
                for item in inventory_items.values():
                    writer.writerow(item)
                    
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e) 
  
# buy_product('apple', 0.60, '2023-12-26')
        


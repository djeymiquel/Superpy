from my_lib2 import *
import pdb
import csv

# Sold Items
def sold_product(product_name: str, sell_price: int):
    
    # Read in the bought.csv file 
    # Find the product in the bought.csv file
    # and look if its already in the sold.csv file
    # if its True break the loop           
    product_found = False
    for row_data in bought_data:
        if row_data["product_name"] == product_name:
            product_found = True
            with open("files/sold.csv", "r") as inp:
                already_sold = False
                sold_data = list(csv.DictReader(inp))
                for row in sold_data:
                    if row_data["ID"] == row["bought_id"]:
                        already_sold = True
                        break
                    
            # If the product is not already sold
            # check if its already expired
            if not already_sold:
                product_id = row_data['ID']
                product_name = row_data['product_name']
                exp_dates = row_data['expiration_date']
                exp_dates = datetime.strptime(exp_dates, '%Y-%m-%d').strftime('%Y-%m-%d')
                expired = False
                if today.strftime('%Y-%m-%d') > exp_dates:
                    expired = True
                    
                    # breakpoint()
                    # If product expired check if it is 
                    # already in the expired.csv file
                    already_in_csv_expired = False
                    for expiry_date in expired_dates:
                        
                        # if True break out of the loop
                        if row_data['ID'] == expiry_date['Exp ID']:
                            already_in_csv_expired = True
                            break
                        
                    # if false write the data to the expired.csv file
                    if not already_in_csv_expired:
                        with open('files/expired.csv', 'a') as out:
                            writer = csv.writer(out)
                            writer.writerow([len(list(csv.reader(open('files/expired.csv')))),
                            row_data["ID"],row_data["product_name"], row_data['buy_date'], row_data['expiration_date']])
                            print(f" '{product_name.title()}' with ID number: {product_id} is expired!")    
                            break
                                 
                # If the product is not expired and not already sold
                # append it to the sold.csv file
                if not expired:
                    with open("files/sold.csv", "a", newline="") as out:
                        writer = csv.writer(out)
                        position = out.tell()
                        sell_date = today
                        if position == 0:
                            writer.writerow(["ID","bought_id","sell_date","sell_price"])
                        writer.writerow([len(list(csv.reader(open("files/sold.csv")))),row_data["ID"],sell_date,sell_price])
                        console.print("OK", style="bold green")
                        break
                     
    # Update the inventory
    # If Product is found and sold update the inventory
    if product_found:
        count = 1
            
        # Check if the product is in stock
        # If True count -1 and break out of the loop
        # write the updated data to the inventory.csv
        in_stock = False
        for row in current_inventory: 
            if row["Product Name"] == product_name:
                in_stock = True
                row["Count"] = str(int(row["Count"]) - count)
                if int(row["Count"]) == 0:
                    current_inventory.remove(row)
                    break
                
        # If false print the message "product 
        # is out of stock"     
        if not in_stock:
            print(f'ERROR: {product_name.title()} not in stock!')
                         
        # 3 Write the updated inventory 
        with open("files/inventory.csv", "w", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=["Product Name","Count","Buy Price","Expiration Date"]) 
            writer.writeheader()
            writer.writerows(current_inventory)
            
    # If the product is not available in SuperPy
    # Print a message  
    else:
        print(f"ValueError: {product_name.title()} not found!")
        
# sold_product('apple', 1.30)
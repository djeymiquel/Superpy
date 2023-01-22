import csv

class CsvReaderParser:
    
    def available_product_reader():
        with open('files/available_items.csv', 'r') as inp:
            data_reader = list(csv.DictReader((inp)))
            for row in data_reader:
                yield row 
        
    def bought_reader():
        with open('files/bought.csv', 'r') as inp:
            data_reader = list(csv.DictReader((inp))) 
            for row in data_reader:
                yield row      
                 
    def sold_reader():
        with open('files/sold.csv', 'r') as inp:
            data_reader = list(csv.DictReader((inp)))
            for row in data_reader:
                yield row    
                   
    def inventory_reader():
        with open('files/inventory.csv', 'r') as inp:
            data_reader = list(csv.DictReader((inp)))
            return data_reader
                     
    def inventory_yesterday_reader():
        with open('files/inventory_yesterday.csv', 'r') as inp:
            data_reader = list(csv.DictReader((inp)))
            for row in data_reader:
                yield row      
                 
    def expired_reader():
        with open('files/expired.csv', 'r') as inp:
            data_reader = list(csv.DictReader((inp)))
            for row in data_reader:
                yield row
         
my_reader = CsvReaderParser
available = my_reader.available_product_reader()
bought_data = my_reader.bought_reader()
sold_data = my_reader.sold_reader()
current_inventory = my_reader.inventory_reader()
# inventory_previeus_day = my_reader.inventory_yesterday_reader()
available_products = my_reader.available_product_reader()
expired_dates = my_reader.expired_reader()


    
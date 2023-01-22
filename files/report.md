
# Technical Implementation Report

## The use of (inner)dictionary

The program makes use of dictionary to store the products data and then check if the product is already in the "inventory.csv" file.
If the product already exist in the inventory.csv file, it increments the count of the product by one.
If the product does not exist, it creates a new entry with the product name as a key for the inner dictionary
and then writes the updated inventory list to the "inventory.csv" file. I chose
this implementation because it allows the program to perform operations in a logical and efficient way

## The use of try and except

The program makes use of try-except blocks to handle various types of errors such as ValueError,
FileNotFoundError, and Exception. This allows the program to continue running even if an error occurs,
and to provide a user-friendly error message in case of an error.
I tought this was the right choice for this implementation because it
allows the program to handle unexpected situations and provide helpful feedback to the user

```python
try:
        if product_name not in (row["store_items"] for row in available_products):
            raise ValueError(f"ValueError: {product_name.title()} not found in available items")

            # code ...

except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e) 

```

## The use of class instances to read and parse csv files

The CsvReaderParser class is a utility class used to read and parse data from various CSV files.
The class contains several methods, each of which is responsible for reading data from a specific CSV file
using the csv.DictReader function, which creates a dictionary for each row in the CSV file,
with the keys as the headers of the CSV file. The methods also use a "yield" statement to return the data as an iterator,
allowing the data to be processed one row at a time, rather than loading the entire data into memory at once.

```python

import csv

class CsvReaderParser:

    def bought_reader():
            with open('files/bought.csv', 'r') as inp:
                data_reader = list(csv.DictReader((inp))) 
                for row in data_reader:
                    yield row

bought_data = my_reader.bought_reader() 

```

This implementation allows for easy access to the data in the CSV files and flexibility in processing the data,
as the methods return the data as a list of dictionaries. Additionally, by using the "yield" statement,
the class avoids loading large amounts of data into memory all at once, which can improve performance and scalability of the program.

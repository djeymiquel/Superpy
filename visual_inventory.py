import matplotlib.pyplot as plt
from my_lib2 import *
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

def visual_inventory_chart(inventory_data):
    # Extract count values from inventory data
    product_names = [row["Product Name"] for row in inventory_data]
    counts = [row["Count"] for row in inventory_data]
    
    # Create a pie chart of count values
    plt.pie(counts, labels=product_names)
    
    # Add title to the chart
    plt.title(" Current Inventory Pie Chart")
    
    # Add the count values next to the product names in the legend
    plt.legend(["{} ({})".format(product_names[i],
    counts[i]) for i in range(len(product_names))], 
    bbox_to_anchor=(1, 0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    
    # Save the chart
    plt.savefig('files/inventory.jpg')
    


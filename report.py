from my_lib2 import *


def revenue_today():
    # Check if sell date equals to today's date
    # if True then sum up the total amount sold
    revenue = 0
    for i in sold_data:
        if i['sell_date'] == today.strftime('%Y-%m-%d'):
            revenue = revenue + float(str(i['sell_price']))
    console.print(f"Today's Revenue so far: {'€ {:,.2f}'.format(revenue)}",style="orange3")


def revenue_yesterday(): 
    # Check if sell date equals to yesterday's date
    # if True the sum up the amount sold yesterday
    revenue = 0
    for i in sold_data:
        if i['sell_date'] == yesterday.strftime('%Y-%m-%d'):
            revenue = revenue + float(str(i['sell_price']))
    console.print(f"Yesterday's Revenue: {'€ {:,.2f}'.format(revenue)}",style="orange3")

  
def revenue_date(date:str):
    # Check if sell date starts with date_str
    # if true, sum up amount sold
    revenue = 0
    date_str = my_date.date_string(date)
    for i in sold_data:
        if i['sell_date'].startswith(date):
            revenue = revenue + float(str(i['sell_price']))
    console.print(f"Revenue from {date_str}:{'€ {:,.2f}'.format(revenue)}",style="orange3")


    
def profit():
    # Check if buy date equals today
    # if true, sum up all prices and add them to bought
    bought = 0
    sold = 0
    for i in bought_data:
        if i['buy_date'] == today.strftime('%Y-%m-%d'):
            bought = bought + float(str(i['buy_price']))
              
    # Check if sell date equals today
    # if true, sum up all prices and add them to sold
    for i in sold_data:
        if i['sell_date'] == today.strftime('%Y-%m-%d'):
            sold = sold + float(str(i['sell_price']))
               
    # substract sold from bought to get today's the profit
    total_profit = bought - sold
    console.print(f"Today's Profit so far: {total_profit:.2f}", style="orange3")

    

def profit_yesterday():
    # Check if buy date equals yesterday
    # if true, sum up all prices and add them to bought
    bought = 0
    sold = 0
    for i in bought_data:
        if i['buy_date'] == yesterday.strftime('%Y-%m-%d'):
            bought = bought + float(str(i['buy_price']))
              
    # Check if sell date equals yesterday
    # if true, sum up all prices and add them to sold
    for i in sold_data:
        if i['sell_date'] == yesterday.strftime('%Y-%m-%d'):
            sold = sold + float(str(i['sell_price']))
               
    # substract sold from bought to get yesterday's profit
    profit = bought - sold
    console.print(f"Yesterday's Profit: {profit:.2f}", style="orange3")
    

def profit_date(date:str):
    # Check if buy en sell date startswith(date_str) 
    # if true, subtract bought from sold to get the profit of a given month
    bought = 0
    sold = 0
    date_str = my_date.date_string(date)
    for i in bought_data:
        if i['buy_date'].startswith(date):
            bought = bought + float(str(i['buy_price']))
            
    for i in sold_data:
        if i['sell_date'].startswith(date):
            sold = sold + float(str(i['sell_price']))
    profit = bought - sold
    console.print(f"profit from {date_str}:{'€ {:,.2f}'.format(profit)}", style="orange3")
    

from my_lib2 import *
from my_lib import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    parser = argparse.ArgumentParser(usage='super.py [OPTION]... or [SUB-COMMANDS]...\nexample: python super.py -ap\nexample: python super.py (Sub-Command) --help', add_help=False,
    description=
    'Buy, Sell products and view various kinds of reports\n\
    about the inventory status, revenue and profit made' 
    )
    
    # Main Parser Arguments
    parser._optionals.title = 'Option'
    parser.formatter_class = ArgumentDefaultsRichHelpFormatter
    parser.add_argument('-at','--advance-time', metavar='', type=int, help='Advance time ', default=argparse.SUPPRESS ,dest='advance_time')
    parser.add_argument('-rt','--retreat-time', metavar='', type=int, help='Retreat time ', default=argparse.SUPPRESS, dest='retreat_time')
    parser.add_argument('-ep','--expired-products', action='store_true', help='Show list of expired products', dest='exp_products', default=argparse.SUPPRESS)
    parser.add_argument('-ap','--available-products', action='store_true', help='Available store products' ,dest='available_products', default=argparse.SUPPRESS)
    parser.add_argument('-h','--help', action='help', help=argparse.SUPPRESS)
    

    subparsers = parser.add_subparsers(title='sub-command', dest="command", metavar='\nbuy\nsell\nreport')
    
    # Buy Sub-command 
    buy_parser = subparsers.add_parser('buy', usage='buy [-p PRODUCT-NAME]...[-P PRICE]...[-e EXP-DATE]...', add_help=False)
    buy_parser._optionals.title = 'All options are required'
    buy_parser.formatter_class = ArgumentDefaultsRichHelpFormatter
    buy_parser.add_argument('-p','--product-name', type=str,  required=True, metavar='', help='name of available product to purchase', default=argparse.SUPPRESS)
    buy_parser.add_argument('-P','--price', type=float, required=True, metavar='', help='price of availaible product to purchase float or int', default=argparse.SUPPRESS)
    buy_parser.add_argument('-e','--expiration-date', type=str, required=True, metavar='', help='expiration date of available product to purchase format(YYYY-MM-DD)', default=argparse.SUPPRESS)
    buy_parser.add_argument('-h','--help', action='help', help=argparse.SUPPRESS)
    
    # Sell Sub-command
    sell_parser = subparsers.add_parser('sell', usage='sell [-p PRODUCT-NAME]...[-P PRICE]...', add_help=False)
    sell_parser._optionals.title = 'All options are required'
    sell_parser.formatter_class = ArgumentDefaultsRichHelpFormatter
    sell_parser.add_argument('-p', '--product-name', type=str, required=True, metavar='', help= 'name of product to sell', default=argparse.SUPPRESS)
    sell_parser.add_argument('-P', '--price', type=float, required=True, metavar='', help='price of product to sell float or int', default=argparse.SUPPRESS)
    sell_parser.add_argument('-h','--help', action='help', help=argparse.SUPPRESS)

    # Report Sub-command
    report_parser = subparsers.add_parser( 'report', usage='report [POSITIONAL]...[OPTION]... ', add_help=False)
    report_parser.add_argument('report', choices=['inventory', 'revenue', 'profit'], default=argparse.SUPPRESS, metavar='\ninventory\nrevenue\nprofit')
    report_parser._optionals.title = 'Option'
    report_parser.formatter_class = ArgumentDefaultsRichHelpFormatter
    group = report_parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--now', action='store_true', help="report inventory's current status", default=argparse.SUPPRESS)
    group.add_argument('-y', '--yesterday', action='store_true', help="report yesterday's inventory, revenue or profit", default=argparse.SUPPRESS, dest='yesterday')
    group.add_argument('-t', '--today', action='store_true', help="report today's revenue or today's profit", default=argparse.SUPPRESS)
    group.add_argument('-d', '--date', metavar='', help="report revenue or profit from a given month (positional) --date YYYY-MM", type=str, default=argparse.SUPPRESS)
    group.add_argument('-h','--help', action='help', help=argparse.SUPPRESS)

    args = parser.parse_args()
    
    
    if args.command == 'buy':
        buy_product(args.product_name, args.price, args.expiration_date)
        visual_inventory_chart(current_inventory)
    
            
    if args.command == 'sell':
        sold_product(args.product_name, args.price)
        visual_inventory_chart(current_inventory)
    
    
    if args.command == 'report':
        if args.report == 'inventory':
            if 'now' in args:
                inventory_now()
            if 'yesterday' in args:
                inventory_yesterday()
    
    
    if args.command == 'report':
        if args.report == 'revenue':
            if 'today' in args:
                revenue_today() 
            if 'yesterday' in args:
                revenue_yesterday()
            if 'date' in args:
                revenue_date(args.date)
    
                
    if args.command == 'report':
        if args.report == 'profit':
            if 'today' in args:
                profit()  
            if 'yesterday' in args:
                profit_yesterday()
            if 'date' in args:
                profit_date(args.date)


    if 'advance_time' in args:
        advanced_time(args.advance_time)
        
        
    if 'retreat_time' in args:
        retreat_time(args.retreat_time)


    if 'exp_products' in args:
        expired()


    if 'available_products' in args:
        available_store_products()
        
if __name__ == "__main__":
    main()
    # print(dir(argparse.ArgumentParser))

# SuperPy

Superpy is a command-line interface tool for a virtual supermarket chain.
With Superpy, you can buy and sell products for a profit, view the current inventory and profit,
and generate reports on the store's revenue and expired products.
This guide will walk you through the various commands
and options available in Superpy and provide examples of how to use them.

## Usage

To access the superpy inventory you need to go to the directory that contains all the files

 ```cli
~/superpy$
```

To see which options are available you can use the following command:

```cli
$python super.py -h
```

here you can get information about the available options and how to use them.

For the sub-commands, you can use --help to see the available options
for example:

```cli
$python super.py buy --help
```

Output:

```cli
usage: buy [-p PRODUCT-NAME]...[-P PRICE]...[-e EXP-DATE]...

Buy Items

options:
  -h, --help            show this help message and exit
  -p, --product-name:   add a product here
  -P, --price:          add a price here in decimal
  -e, --expiration-date
                        : add an expiration date here in the format YYYY-MM-DD
```

## CLI Interactions

Examples of how to interact with the superpy inventory system
To see which products are available in to buy you can use the following command:
$ python super.py --available-products

To buy a product you can use the following command:
make sure that you use the right format for the price (decimal numbers) and the expiration date YYYY-MM-DD

### Buy

```cli
$python super.py buy --product-name orange --price 0.65 --expiration-date 2023-01-10
```

To sell a product use this sub-command:

### Sell

```cli
$python super.py sell --product-name orange --price 1.60
```

### Visual stock pie chart

After you bought the second item a visual stock representation can be found
in the superpy directory with the name inventory.jpg

### Report

To display different kinds of reports you can use these sub commands.
for example if you want to show the current inventory:

```cli
$python super.py report inventory --now
```

if you want to see today's profit, you can use this command:

```cli
$python super.py report profit --today
```

if you want to see the revenue of a certain date, you can use this command:
make sure you use this YYYY-MM format for the date

```cli
$python super.py report revenue --date 2022-01
```

To advance the date, you can use this command with an int as a value:

```cli
$python super.py --advance-time 2
```

To see what products were expired, you can use this command:

```cli
$python super.py --expired-products
```

Written by Djephaniah Miquel\
<djey.zakelijk@gmail.com>

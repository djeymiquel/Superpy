from my_lib import *

def test_available_product_reader():
    for i in available_products:
        assert len(i) == 1
        
def test_bought_reader():
    for i in bought_data:
        assert len(i) == 5
        
def test_sold_reader():
    for i in sold_data:
        assert len(i) == 4
    
def test_inventory_reader():
    for i in current_inventory:
        assert len(i) == 4
        
def test_expired_reader():
    for i in expired_dates:
        assert len(i) == 5
        
        
        
        
        
        
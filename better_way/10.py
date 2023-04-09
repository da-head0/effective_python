if count := fresh_fruit.get('apple', 0):
    make_juice(count)
else:
    out_of_stock()
    
if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()
    
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
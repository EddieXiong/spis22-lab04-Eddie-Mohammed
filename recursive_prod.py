def rec_product(a, b):
    if a == 1:
        return b
    return b + rec_product(a-1, b)
print (rec_product(10, 5))
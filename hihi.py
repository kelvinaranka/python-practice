from functools import reduce

#sample data
products = ['laptop', 'mouse', 'keyboard', 'monitor']
prices = [800, 25, 150, 400] 

#MAP add 10% tax to every price
taxed_prices = list(map(lambda prices: prices *1.10, prices))
print(taxed_prices)

#FILTER only keep products that cost more than $50 after tax
expensive = list(filter(lambda prices: prices > 50, taxed_prices))
print(expensive)

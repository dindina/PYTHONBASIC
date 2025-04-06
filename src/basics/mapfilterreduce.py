products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200, "in_stock": True},
    {"name": "Book", "category": "Books", "price": 25, "in_stock": True},
    {"name": "Smartphone", "category": "Electronics", "price": 800, "in_stock": False},
    {"name": "T-shirt", "category": "Apparel", "price": 30, "in_stock": True},
    {"name": "Ebook", "category": "Books", "price": 15, "in_stock": True},
    {"name": "Headphones", "category": "Electronics", "price": 150, "in_stock": True},
    {"name": "Jeans", "category": "Apparel", "price": 75, "in_stock": False},
]

print(type(products))
# find all product name in stock , with category electronics

sublist = [ item['name'] for item in products  ]

print(sublist)

sublist = [ item['name'] for item in products  if item['in_stock'] == True and item['category'] == 'Electronics']
print(sublist)


# use lambda 

in_stock_products = filter(lambda product: product["in_stock"] and product['category'] == 'Electronics', products)
print("In-stock products:" , in_stock_products)
for product in in_stock_products:
    print(f"- {product['name']}")
print("-" * 30)


# map 

maplist = map( lambda product : product['name']+"-"+str(product['in_stock']) , products)
print(list(maplist))

from collections import Counter

list11 = [1,2,2,2]

bb = Counter(list11)
print(bb)

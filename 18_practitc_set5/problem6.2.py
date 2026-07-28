def most_expensive_product(products):

    return max(products.items(), key=lambda x: x[1])
product ={

       "Laptop": 90000,
       "Phone": 70000,
       "Tablet": 55000,
       "Moniter": 35000,
    }

product,price = most_expensive_product(product)

print(f"the most expensive product is '{product}' with price {price}.")

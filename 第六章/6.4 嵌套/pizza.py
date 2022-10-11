#存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extre cheese'],
    }
# 概述所点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['topping']:
    print("\t" + topping)
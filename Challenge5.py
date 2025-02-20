import numpy as np
import random as random

fruit_prices = {
    "apple": round(random.uniform(1.0, 3.0), 2),
    "banana": round(random.uniform(1.0, 3.0), 2),
    "orange": round(random.uniform(1.0, 3.0), 2),
    "grape": round(random.uniform(1.0, 3.0), 2),
    "cherry": round(random.uniform(1.0, 3.0), 2),
    "pineapple": round(random.uniform(1.0, 3.0), 2)
}

expensive_fruits = {}

for x in fruit_prices:
    if fruit_prices[x] > 2.0:
        expensive_fruits.update({x: fruit_prices[x]})

print(expensive_fruits)
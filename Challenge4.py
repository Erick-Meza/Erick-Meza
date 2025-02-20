import random as random
import numpy as np

fruit_prices = {
    "apple": round(random.uniform(1.0, 3.0), 2),
    "banana": round(random.uniform(1.0, 3.0), 2),
    "orange": round(random.uniform(1.0, 3.0), 2),
    "grape": round(random.uniform(1.0, 3.0), 2),
    "cherry": round(random.uniform(1.0, 3.0), 2),
    "pineapple": round(random.uniform(1.0, 3.0), 2)
}

print("Generated fruit prices:", fruit_prices)
print(np.mean(list(fruit_prices.values())))

from collections import defaultdict
import random

class DataStore:
    def __init__(self):
        self.products = {}
        self.sales = defaultdict(list)
        self.user_data = defaultdict(dict)
        self.suppliers = defaultdict(list)

    def load_sample_data(self):
        for i in range(1, 11):
            self.products[i] = {
                "name": f"Product_{i}",
                "stock": random.randint(10, 100),
                "cost": random.randint(5, 50),
                "profit": random.randint(10, 80),
            }
            self.sales[i] = [random.randint(0, 50) for _ in range(4)]
            for j in range(3):
                self.suppliers[i].append({
                    "supplier_id": f"s{i}{j}",
                    "cost": random.randint(5, 15),
                    "delivery_time": random.randint(1, 5),
                    "reliability": random.random()
                })

    def get_top_k_selling(self, k):
        return sorted(self.sales.items(), key=lambda x: sum(x[1]), reverse=True)[:k]

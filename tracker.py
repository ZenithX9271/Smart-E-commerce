import heapq

def top_k_products(sales_data, k):
    heap = []
    for pid, weeks in sales_data.items():
        total = sum(weeks)
        heapq.heappush(heap, (-total, pid))  # max-heap
    return [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]

def low_stock_products(products, k):
    heap = []
    for pid, data in products.items():
        heapq.heappush(heap, (data['stock'], pid))
    return [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]

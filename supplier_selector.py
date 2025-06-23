import heapq

def select_best_supplier(suppliers_list):
    heap = []
    for supplier in suppliers_list:
        score = (
            supplier['reliability'] * 0.5 +
            (1 / supplier['delivery_time']) * 0.3 +
            (1 / supplier['cost']) * 0.2
        )
        heapq.heappush(heap, (-score, supplier))  # max heap
    return heapq.heappop(heap)[1] if heap else None

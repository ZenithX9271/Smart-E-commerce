from datastore import DataStore
from optimizer import optimal_restock
from tracker import top_k_products, low_stock_products
from supplier_selector import select_best_supplier

def main():
    ds = DataStore()
    ds.load_sample_data()

    print("\nDP: Optimal Restock Plan (Budget = 100)")
    restock, total_profit = optimal_restock(ds.products, 100)
    for pid in restock:
        print(f"Restock {ds.products[pid]['name']} | Profit: {ds.products[pid]['profit']}")
    print(f"Total Expected Profit: {total_profit}")

    print("\nHeap: Top-3 Selling Products")
    for pid in top_k_products(ds.sales, 3):
        print(f"{ds.products[pid]['name']} → Weekly Sales: {ds.sales[pid]}")

    print("\nHeap: Low-Stock Alerts (3)")
    for pid in low_stock_products(ds.products, 3):
        print(f"{ds.products[pid]['name']} | Stock: {ds.products[pid]['stock']}")

    print("\nPQ: Supplier Selection Example (Product 1)")
    best_supplier = select_best_supplier(ds.suppliers[1])
    print(f"Selected Supplier: {best_supplier}")

if __name__ == "__main__":
    main()

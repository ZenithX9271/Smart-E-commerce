#Smart E-commerce Inventory Recommender System

A **DSA-rich, real-world Python project** that simulates an intelligent inventory recommender for e-commerce platforms. It helps decide **what products to restock**, **which suppliers to choose**, and **which items are in-demand or running low** — all powered by advanced algorithms and data structures.

> Designed to showcase core DSA concepts: **Dynamic Programming**, **Heaps**, **Priority Queues**, and **HashMaps**.

---

## 📌 Features

✅ Optimal restocking using **0/1 Knapsack DP**  
✅ Track **Top-K bestsellers** with **Max Heap**  
✅ Monitor **Low-stock items** with **Min Heap**  
✅ Choose **best suppliers** using **Priority Queue** with multi-factor ranking  
✅ In-memory **HashMap-based datastore** for products, sales, and suppliers

---

## 📂 Project Structure

```bash
smart_inventory/
│
├── main.py                   # Entry point that ties everything together
├── optimizer.py              # DP for optimal restocking (0/1 Knapsack)
├── tracker.py                # Heaps for top-k and low-stock product tracking
├── supplier_selector.py      # Priority Queue to select best supplier
├── datastore.py              # Simulated in-memory database (HashMap-based)

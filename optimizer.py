def optimal_restock(products, budget):
    n = len(products)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(products.items())

    for i in range(1, n + 1):
        pid, data = item_list[i - 1]
        cost = data['cost']
        profit = data['profit']
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + profit)
            else:
                dp[i][b] = dp[i - 1][b]

    selected = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            pid, _ = item_list[i - 1]
            selected.append(pid)
            b -= products[pid]['cost']

    return selected, dp[n][budget]

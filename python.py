def sort_products(products):
    return sorted(
        products,
        key=lambda x: (x["priority"] * x["demand"]) / x["cost"],
        reverse=True
    )


def greedy(products, capacity, budget):
    products = sort_products(products)

    selected = []
    used_space = 0
    used_budget = 0
    profit = 0

    for p in products:
        if used_space + p["space"] <= capacity and \
           used_budget + p["cost"] <= budget:

            selected.append(p)
            used_space += p["space"]
            used_budget += p["cost"]
            profit += p["profit"]

    return selected, used_space, used_budget, profit


def dynamic_programming(products, capacity, budget):
    n = len(products)

    # dp[space][budget] = maximum profit
    dp = [[0] * (budget + 1) for _ in range(capacity + 1)]

    for p in products:
        space = p["space"]
        cost = p["cost"]
        profit = p["profit"]

        for s in range(capacity, space - 1, -1):
            for b in range(budget, cost - 1, -1):
                dp[s][b] = max(
                    dp[s][b],
                    dp[s - space][b - cost] + profit
                )

    selected = []
    s = capacity
    b = budget

    for i in range(n - 1, -1, -1):
        p = products[i]

        if s >= p["space"] and b >= p["cost"]:
            if dp[s][b] == dp[s - p["space"]][b - p["cost"]] + p["profit"]:
                selected.append(p)
                s -= p["space"]
                b -= p["cost"]

    selected.reverse()

    used_space = sum(p["space"] for p in selected)
    used_budget = sum(p["cost"] for p in selected)
    profit = sum(p["profit"] for p in selected)

    return selected, used_space, used_budget, profit
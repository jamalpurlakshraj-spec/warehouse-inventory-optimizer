from copy import deepcopy

from flask import Flask, render_template, request
from python import greedy, dynamic_programming, sort_products

app = Flask(__name__)


DEFAULT_PRODUCTS = [
    {
        "name": "Laptop",
        "demand": 90,
        "priority": 5,
        "cost": 50000,
        "space": 10,
        "profit": 12000,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=900&q=80"
    },
    {
        "name": "Phone",
        "demand": 150,
        "priority": 5,
        "cost": 25000,
        "space": 5,
        "profit": 8000,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=80"
    },
    {
        "name": "Monitor",
        "demand": 70,
        "priority": 3,
        "cost": 15000,
        "space": 8,
        "profit": 4000,
        "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=900&q=80"
    },
    {
        "name": "Keyboard",
        "demand": 200,
        "priority": 2,
        "cost": 2000,
        "space": 2,
        "profit": 1000,
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=900&q=80"
    },
    {
        "name": "Printer",
        "demand": 40,
        "priority": 4,
        "cost": 20000,
        "space": 12,
        "profit": 5000,
        "image": "https://images.unsplash.com/photo-1550009158-9ebf69173e03?auto=format&fit=crop&w=900&q=80"
    }
]

products = deepcopy(DEFAULT_PRODUCTS)


def handle_product_actions():
    action = request.form.get("action")

    if action == "add_product":
        name = request.form.get("name", "").strip()
        image = request.form.get("image", "").strip()

        if name:
            new_product = {
                "name": name,
                "demand": int(request.form.get("demand", 0) or 0),
                "priority": int(request.form.get("priority", 0) or 0),
                "cost": int(request.form.get("cost", 0) or 0),
                "space": int(request.form.get("space", 0) or 0),
                "profit": int(request.form.get("profit", 0) or 0),
                "image": image or "https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=900&q=80",
            }

            existing = any(p["name"].lower() == name.lower() for p in products)
            if not existing:
                products.append(new_product)

    elif action == "delete_product":
        product_name = request.form.get("product_name", "").strip()
        products[:] = [p for p in products if p["name"].lower() != product_name.lower()]

    elif action == "reset_products":
        products[:] = deepcopy(DEFAULT_PRODUCTS)


@app.route("/", methods=["GET", "POST"])
def index():
    capacity = 30
    budget = 100000

    if request.method == "POST":
        action = request.form.get("action")

        if action == "optimizer":
            capacity = int(request.form.get("capacity", capacity) or capacity)
            budget = int(request.form.get("budget", budget) or budget)
        else:
            handle_product_actions()

    sorted_products = sort_products(products)

    g_items, g_space, g_budget, g_profit = greedy(
        products, capacity, budget
    )

    d_items, d_space, d_budget, d_profit = dynamic_programming(
        products, capacity, budget
    )

    return render_template(
        "index.html",
        products=sorted_products,
        capacity=capacity,
        budget=budget,
        greedy_items=g_items,
        greedy_space=g_space,
        greedy_budget=g_budget,
        greedy_profit=g_profit,
        dp_items=d_items,
        dp_space=d_space,
        dp_budget=d_budget,
        dp_profit=d_profit
    )


if __name__ == "__main__":
    app.run(debug=True)

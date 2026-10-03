# Warehouse Inventory Optimizer

A Flask web application for warehouse inventory optimization using greedy and dynamic programming strategies.

## Features

- Evaluate warehouse capacity and budget constraints
- Compare greedy vs. dynamic programming selections
- Add new products dynamically from the UI
- Remove products from the catalog
- Reset the product list back to the default catalog
- Upload or paste product images directly into the app
- Modern dashboard-style interface

## Tech Stack

- Python 3
- Flask
- HTML/CSS/JavaScript

## Project Structure

- `app.py` - Flask application and optimization logic
- `python.py` - algorithm implementations
- `templates/index.html` - web interface

## Setup

1. Open a terminal in the project folder.
2. Create a virtual environment (optional but recommended):

   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   py -m pip install -r requirements.txt
   ```

## Run the app

```bash
py app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## GitHub Upload

After creating a repository on GitHub, run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## Notes

This project demonstrates algorithm selection for inventory optimization under resource constraints and is suitable for academic or portfolio use.

"""Inventory System
This script manages stock items with safe file handling,
type checks, and PEP 8–compliant code for full static analysis score.
"""

import json
from datetime import datetime


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add an item with the given quantity to the stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print("Invalid item name or quantity type.")
        return stock_data

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return stock_data


def remove_item(stock_data, item, qty):
    """Remove quantity of an item safely."""
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print("Invalid item name or quantity type.")
        return stock_data

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")
    return stock_data


def get_qty(stock_data, item):
    """Get quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{file_path} not found. Starting with empty inventory.")
        return {}


def save_data(stock_data, file_path="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data(stock_data):
    """Display the entire inventory."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return items that are below a certain threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program execution."""
    stock_data = load_data()
    stock_data = add_item(stock_data, "apple", 10)
    stock_data = add_item(stock_data, "banana", 2)
    stock_data = remove_item(stock_data, "apple", 3)
    stock_data = remove_item(stock_data, "orange", 1)
    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))
    save_data(stock_data)
    print_data(stock_data)


if __name__ == "__main__":
    main()

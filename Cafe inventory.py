import csv

inventory_rows = [
    ["item_name", "price", "quantity_in_stock"],
    ["Coffee", "3.50", "50"],
    ["Tea", "2.75", "40"],
    ["Muffin", "2.25", "30"],
]

with open("inventory_sample.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(inventory_rows)

sales_rows = [
    ["item_name", "quantity"],
    ["Coffee", "3"],
    ["Muffin", "2"],
    ["Tea", "5"],
]

with open("sales_sample.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(sales_rows)

print("Created inventory_sample.csv and sales_sample.csv")
from typing import List, Dict

def load_inventory(filename: str) -> List[Dict[str, str]]:
    '''Load inventory from CSV into a list of dicts.'''
    # TODO
    inventory = []
    with open(filename, newline = "", encoding="utf-8" ) as d: # opening the file, and encoding it to convert to bytes for python to read. 'd' is what I chose to name the file.
      reading_files = csv.DictReader(d) #reading through the file.
      for r in reading_files:
        inventory.append(r)
    return inventory
   # raise NotImplementedError("Implement load_inventory") commenting this out because otherwise our code with crash!


def load_sales(filename: str) -> List[Dict[str, str]]:
    '''Load sales from CSV into a list of dicts.'''
    # TODO
    sales = []
    with open(filename, newline = "", encoding="utf-8") as d: # opening the file, and encoding it to convert to bytes for python to read. 'd' is what I chose to name the file.
      reading_files = csv.DictReader(d) #reading through the file.
      for r in reading_files:
        sales.append(r)
    return sales
   # raise NotImplementedError("Implement load_sales")


def process_sales(inventory: List[Dict[str, str]], sales: List[Dict[str, str]]) -> float:
    '''
    Process each sale:
      - reduce quantity_in_stock
      - compute total revenue
    Return total revenue as float.
    '''
    # TODO
    total_revenue = 0.0 #starts the counter at 0, like a fresh start.
    for sale in sales: #Looking through every sale.
      name = sale["item_name"] #looks at a specific item, saves it in a variable.
      quantity = int(sale["quantity"]) #converts the string into an integer.
      for item in inventory: #Looking through every item in the inventory.
        if item["item_name"] == name:
          price = float(item["price"])
          stocks = int(item["quantity_in_stock"])
          selling = min(quantity, stocks) #looking for which is lower, the quantity or stock.
          total_revenue = total_revenue + (selling * price) #revenue is calculated by adding the total_revenue to the item sold multiplied by its price.
          item["quantity_in_stock"] = str(stocks-selling) #updates inventory by removing whatever is already sold.
          break
    return total_revenue
    #raise NotImplementedError("Implement process_sales")


def low_stock_items(inventory: List[Dict[str, str]], threshold: int = 5) -> List[Dict[str, str]]:
    '''Return list of items with quantity_in_stock < threshold.'''
    # TODO
    #raise NotImplementedError("Implement low_stock_items")
    low_stock = []
    for item in inventory: #Looking through every item in the inventory.
      if int(item["quantity_in_stock"]) < threshold: #checks if the quantity is below the threshold.
        low_stock.append(item) # if yes, then it appends it into the low_stock list. If not, then nothing happens.
    return low_stock
def main() -> None:
    '''
    Main program:
      - Load inventory and sales
      - Process sales
      - Print total revenue
      - Print low-stock items
    '''
    inventory = load_inventory("inventory_sample.csv") #calling the function.
    sales = load_sales("sales_sample.csv") #calling the function.
    revenue = process_sales(inventory, sales) #this is getting the revenue.
    print("The total revenue is: ", revenue) #printing out the revenue.
    print("These are the low stock items: ")#printing out the low stock items.
    for item in low_stock_items(inventory):
      print(item)#prints out any item that is in the low stock section.
    if not low_stock_items(inventory):
      print("There are no items that are low in stock.") # prints this line if there are no items that are low in stock.
    #raise NotImplementedError("Implement main")
main()

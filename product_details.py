"""This program provides the Product details
Retrieves the Product details and Exit
"""
from dataclasses import dataclass, asdict
import json
import os



@dataclass
class Product():
    product_name: str
    product_category: str
    product_id: str

'''class Product():
    """This has the data of Product
    """
    def __init__(self, product_name, product_category, product_id):
        self.product_name = product_name
        self.product_category = product_category
        self.product_id = product_id
    def __repr__(self):
        return f"product_name = {self.product_name}, product_category = {self.product_category}, product_id = {self.product_id} \n"'''

product_dict = dict()

#persistence = "Product_details.txt"
DATASTORE_PATH = "Product_details.json"

def add_Product():

    """This adds Product into the dictionary
    """
    product_name = input("Enter product_name:")
    product_category = input("Enter product_category:")
    product_id = input("Enter prooduct Id:")
    #Product = Product(product_name, product_category, product_id)
    #Product_dict[product_id] = Product
    product = Product(product_name=product_name, product_category=product_category, product_id=product_id)
    product_dict[product_id] = asdict(product)
    #with open(persistence, mode = 'a', encoding= "utf-8") as Product_file:
    #    Product_file.write(str(Product))
    with open(DATASTORE_PATH, mode = 'w', encoding= "utf-8") as product_file:
        json.dump(product_dict, product_file, indent=4)

def fetch_Product():
    """This fetches the Product details 
        If product_id id matches
    """
    product_id = input("Enter Product product_id id: ")
    if product_id in product_dict:
        #Product = Product_dict[product_id]
        product = Product(**product_dict[product_id])
        print(f"product_name = {product.product_name}")
        print(f"product_category = {product.product_category}")
        print(f"product_id = {product.product_id}")
    else:
        print("Product not found")

def initialize_data():
    """This is for initializing data
    """
    if os.path.exists(DATASTORE_PATH):
        with open(DATASTORE_PATH, mode= 'r', encoding="utf-8") as Product_file:
            global product_dict
            product_dict = json.load(Product_file)




def menu():
    """This is for the Menu of Application
    """
    initialize_data()
    while True:
        #add_Product()
        choices = input("Enter your choices 1 for adding, 2 for fetching and 3 for exit ")
        if choices.strip() == '1':
            add_Product()
        elif choices.strip() == '2':
            #fetch_Product
            fetch_Product()
        else:
            break
    print("Thanks*****************")


if __name__ == '__main__':
    menu()
from urllib.request import urlopen

class ProductEngine:

    def __init__(self, name):
        self.name = name
        self.products = []    # creates a new empty list for products

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        html = urlopen("https://supremenewyork.com/shop/bags/lmgr9ly8q/yntmgxvhb")
        print(html.read())
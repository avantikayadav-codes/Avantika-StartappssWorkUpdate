class Product:
    def __init__(self,product_id,product_name,category,brand,price,stock,rating,warranty):
        self.product_id=product_id
        self.product_name=product_name
        self.category=category
        self.brand=brand
        self.price=price
        self.stock=stock
        self.rating=rating
        self.warranty=warranty

    def buy(self):
        n=int(input("Enter quantity of product you want to buy"))
        if self.stock>n:
            print("Item Ordered!")

    def add_to_cart(self):
        print(self.product_id,":",self.product_name,"Added to cart!")

    def update_stock(self):
        n=int(input("Enter updated quantity of product"))
        self.stock=n
        print("Updates Stock:",self.stock)

    def show_details(self):
        print("Product ID :",self.product_id)
        print("Product Name :",self.product_name)
        print("Category :",self.category)
        print("Brand :",self.brand)
        print("Price :",self.price)
        print("Stock :",self.stock)
        print("Rating :",self.rating)
        print("Warranty :",self.warranty)

    def apply_discount(self):
        n=int(input("Enter how much discount you want!"))
        final_price=self.price-(self.price*n/100)
        print("Real price:",self.price)
        print("Discount Applied! :",n,"%")
        print("Discounted Price:",final_price)

obj=Product(
    101,
    "Wireless Mouse",
    "Electronics",
    "Logitech",
    999,
    50,
    4.5,
    "1 Year"
)

obj.buy()
obj.add_to_cart()
obj.update_stock()
obj.show_details()
obj.apply_discount()
class FoodOrder:
    def __init__(self,order_id,customer_name,restaurant_name,food_item,quantity,price,delivery_address,payment_status):
        self.order_id=order_id
        self.customer_name=customer_name
        self.restaurant_name=restaurant_name
        self.food_item=food_item
        self.quantity=quantity
        self.price=price
        self.delivery_address=delivery_address
        self.payment_status=payment_status

    def place_order(self):
        print("Order Placed Successfully")

    def cancel_order(self):
        print("Order Cancelled Successfully")

    def track_order(self):
        print("Your Order is On the Way")

    def make_payment(self):
        self.payment_status="Paid"
        print("Payment Successful")

    def show_order(self):
        print("Order ID :",self.order_id)
        print("Customer Name :",self.customer_name)
        print("Restaurant Name :",self.restaurant_name)
        print("Food Item :",self.food_item)
        print("Quantity :",self.quantity)
        print("Price :",self.price)
        print("Delivery Address :",self.delivery_address)
        print("Payment Status :",self.payment_status)


obj=FoodOrder(
    101,
    "Avantika",
    "Dominos",
    "Farmhouse Pizza",
    2,
    699,
    "Indore",
    "Pending"
)

obj.place_order()
obj.make_payment()
obj.track_order()
obj.show_order()
obj.cancel_order()
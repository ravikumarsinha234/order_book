class EachOrder:
    def __init__(self,order_id,side,price,quantity):
        self.order_id = order_id #assuming order id to be unique
        self.side = side # It will be 'B' for buy and 'S' for sell
        self.price = price
        self.quantity = quantity

class OrderBook:
    def __init__(self):
        self.orders={}

    def OnNewOrder(self,order):
        self.orders[order.order_id] = order

    def OnChangeOrder(self,change_order):
        if change_order.order_id in self.orders:
            order = self.orders[change_order.order_id] #order to be updated
            order.price = change_order.new_price
            order.quantity = change_order.new_quantity
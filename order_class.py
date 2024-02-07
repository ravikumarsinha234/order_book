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

    def OnCancelOrder(self,cancel_order):
        if cancel_order.order_id in self.orders:
            del self.orders[cancel_order.order_id]

    def PrintOrderBook(self):
        buyers = []
        sellers = []

        for order_id,order_details in self.orders.items():
            if order_details.side=='B':
                buyers.append(order_details)
            else:
                sellers.append(order_details)

        print('Buys:')
        buyers.sort(key=lambda x:x.price,reverse=True)
        self._print_orders(buyers)

        print('\n')

        print('Sells:')
        sellers.sort(key=lambda x:x.price,reverse=True)
        self._print_orders(sellers)


    def _print_orders(self,orders):
        agg_orders = {}
        for single_order in orders:
            if single_order.price in agg_orders:
                agg_orders[single_order.price] += single_order.quantity
            else:
                agg_orders[single_order.price] = single_order.quantity

        for price,quantity in agg_orders.items():
            print(f'Price: {price} | Quantity: {quantity}')
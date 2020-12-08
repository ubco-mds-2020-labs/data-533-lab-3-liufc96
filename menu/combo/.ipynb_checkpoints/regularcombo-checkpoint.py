class Regularcombo():
    """docstring for ."""
    def __init__(self, burger = ["big_mac"], snack = ["fries"], drink = ["coca"]):
        self.burger = burger
        self.snack = snack
        self.drink = drink
    def burger_custom(self, extra):
        self.burger.append(extra)
    def snack_custom(self, extra):
        self.snack.append(extra)
    def drink_custom(self, extra):
        self.drink.append(extra)
    def display(self):
        print("burger:{},snack:{},drink:{}".format(self.burger, self.snack, self.drink))
    def total_price(self):
        total = (len(self.burger)*4.99 + len(self.snack)*2.99 + 1.99)*1.15
        print("total price is:{} CAD(Tax included)".format(total))

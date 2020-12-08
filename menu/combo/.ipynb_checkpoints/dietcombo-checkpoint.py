from menu.combo.regularcombo import Regularcombo

class Dietcombo(Regularcombo):
    """docstring for ."""
    def __init__(self, burger = ["cheeseburger"], snack = ["fries"], drink = ["diet","coca"]):
        Regularcombo.__init__(self, burger, snack, drink)
    def calories_check(self):
        if self.drink[0] == "diet":
            total = (len(self.burger))*200 + (len(self.snack))*100
        else:
            total = (len(self.burger))*200 + (len(self.snack))*100 + (len(self.drink))*50
        if total > 500:
            print("warning: calories higher than standard!!!")
    def drink_check(self):
        if self.drink[0]!= "diet":
            print("warning: drink is not diet!")

    def burger_cal_control(self):
        if len(self.burger) > 1:
            self.burger = self.burger[0:1]
            print("Only regurlar burger provided in diet combo")

from item import ItemC


############ inheritance #######################
class Phone(ItemC):
    pay_rate = 0.5
    def __init__(self, name, price, quantity=0,is_broken =0):
        super().__init__(name, price, quantity)

        assert is_broken >=0, f"Broken Phone {is_broken}"
        self.is_broken = is_broken
    
phoneX = Phone("nokia",500, 6, 1)    
print(phoneX.calculate_total_price())
print(ItemC.all)
print(Phone.all)
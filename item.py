import csv

# the simplest class
class ItemA:
    pass

# the first instance
item1 = ItemA()
item1.name = "phone"
item1.price = 100
item1.quantity = 2

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))


#class with a method
class ItemB:
    def calculate_total_price(self,x,y):
        return x*y

# the second instance
item1 = ItemB()
item1.name = "phone"
item1.price = 100
item1.quantity = 2
# print(item1.calculate_total_price(item1.price,item1.quantity))


item2 = ItemB()
item2.name = "laptop"
item2.price = 500
item2.quantity = 5
# print(item2.calculate_total_price(item2.price,item2.quantity))


#class using a constructor
class ItemC:
    pay_rate = 0.8 # class attribute 
    all = []
    def __init__(self, name:str , price:float, quantity=0):  # validate parameters data type 
        # print("I'm created ") 

        #run validation to the received parameters
        assert price >= 0, f" price {price} is not greater than zero"
        assert quantity >= 0, f" quantity {quantity} is not greater than zero" 

        #assign to self pbject
        #self._name = name   #single underscore to render the attribute private or can't be overriden by the user ( private )
        self.__name = name # double underscore to render the attribute unaccessible completely  from the instance level )( protected )
        self.__price = price
        self.quantity = quantity 

        #code to execute 
        ItemC.all.append(self)

    @property
    def price(self):
        return self.__price    
    

    def apply_discount(self):
        # self.price = self.price * ItemC.pay_rate  # not able to be overriden from the instance level
        self.__price = self.__price * self.pay_rate  # able to be overriden from the instance level


    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value



    @property  #getter 
    def name(self): #render this aattribute can't be overriden by the user 
        return self.__name
    
    @name.setter  #setter 
    def name(self, value):
        self.__name = value 

    def calculate_total_price(self):  # no more parameetes need
        return self.__price * self.quantity
    
    def __str__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity})" 

    def __repr__(self):
        #return f"ItemC('{self.name}', {self.price}, {self.quantity})"    
        return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity})" 
    
    @classmethod  #instantiating from csv need  class method using class method decorator where the method take class as its 1st parameter 
    def instantiate_from_csv(cls):
        with open('items.csv' , 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            #print(item)
            ItemC(
                name=item.get('name'),
                price =float(item.get('price')),
                #quantity = int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer() #return true if a float is intger 
        elif isinstance(num, int):
            return True
        else:
            return False

    def __connect(self):  ## private methods to work only in the class level 
        pass
    def  __open_port(self):
        pass

    def send_email(self):
        self.__open_port() 
        self.__connect()
        

# item1 = ItemC("phone", 100, 2)
#print(item1.calculate_total_price())
# item1.apply_discount()
# print(item1.price)

# item2 = ItemC("laptop", 1000, 5)
# item2.has_numpad = False ## instance attribute created after instance created 
# item2.pay_rate = 0.7
#print(item2.calculate_total_price())
# item2.apply_discount()   
# print(item2.price) 

# print(ItemC.pay_rate) #class atrribute is accessible from the class level
# print(item1.pay_rate) # class attribute is accessible from the instance level
# print(item2.pay_rate) # class attribute is accessible from the instance level

# print(ItemC.__dict__) # magic attribute to get all attribue of a class 
# print(item1.__dict__) # magic attribute to get all attribue of an instance 
# print(item2.__dict__) # magic attribute to get all attribue of an instance 

# item1 = ItemC("Phone", 100, 1)
# item2 = ItemC("Laptop", 1000, 3)
# item3 = ItemC("Cable", 10, 5)
# item4 = ItemC("Mouse", 50, 5)
# item5 = ItemC("Keyboard", 75, 5)

ItemC.instantiate_from_csv()

# print(ItemC.all[0])
# itemX = ItemC.all[0]
# print(itemX.is_integer(5))
# print(ItemC.is_integer(99))

######### multiple inheritance 
 
class ItemD(ItemA,ItemB):
    pass

item5 = ItemD()

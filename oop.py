from item import ItemC
from phone import Phone

## encapsulation 
## restrict access to the instance attribute and mofify the attributes only through methods 

itemX = ItemC("iphone", 200)

#itemX.name = "android" # can't be changed

print(itemX.name)

itemX.name = "android"

print(itemX.name)

itemX.apply_increment(0.2)
itemX.apply_discount()
print(itemX.price)


### abstraction is showing the user the necessary information from the instances  and methods 
#  only and hiding all the unnecessary methods  using double __ so it can be called from the class level 
# itemX.__connect()  ## unallowed as it's a private method 

### polymorphism 

phone1 = Phone("xiaomi", 100, 5)
phone1.apply_discount()
print(phone1.price)
itemX.apply_discount()
print(itemX.price)
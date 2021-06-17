class SuperMarket:
    """ THIS IS MY SUPERMARKET"""
    def __init__(self):   #Creating Default COnstructor
        print("Hi I am Constructor")




bread = SuperMarket()
bread.brand="ABC"
print(bread.brand)
biscuit = SuperMarket()
biscuit.price=25
print(biscuit.price)
shampoo = SuperMarket()
shampoo.brand="DDD"
shampoo.price=10
shampoo.discount=5
print(shampoo.__dict__)
#rice = SuperMarket("Basmati",100)


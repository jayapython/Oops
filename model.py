class SuperMarket:
    """ THIS IS MY SUPERMARKET"""
    manufa="Harshi SuperMarket"
    marketer="ammu"
    def __init__(self,brand,price,discount=None):
        self.brand=brand
        self.price=price
        self.discount=discount
        print("ceheck")
        




bread = SuperMarket("ABC",25,2)
print(bread.brand)
biscuit = SuperMarket("DEF",10,5)
print(biscuit.discount)
shampoo = SuperMarket("GHI",5,3)
print(shampoo.__dict__)
rice = SuperMarket("Basmati",100)
rice.manufa='Rice Mill'
print(rice.manufa)
print(shampoo.manufa)

print(SuperMarket.manufa)
print(SuperMarket.marketer)


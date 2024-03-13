import csv

class Item:

    # class attributes
    all=[] # list to store all objects
    pay_rate = 1.0 # declared global so that the value remains accesible to calculate_total_price() which is outside of apply_discount() scope
    discount_applicable=0


    def __init__(self,name:str,price:float,quantity=1): #type-hints
        
        # Validation
        assert price >=1, f"Price of {name} must be atleast 1!"
        assert quantity >=1, f"Quantity of {name} must be atleast 1!"

        # Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

        # Append object to list
        Item.all.append(self)

        # Reset discount flag for every instance
        Item.discount_applicable=0

    # encapsulation example 

    def apply_discount(self,pay_rate=0.8): # sets discount flag for total_cost calculation and global default discounted pay_rate of 20%
        Item.discount_applicable=1
        self.pay_rate = pay_rate
        # self.price=self.price * self.pay_rate


    def calculate_total_cost(self):
        if Item.discount_applicable:
            return round((self.pay_rate * self.price) * self.quantity,2) # python will first check if pay_rate is value available for current instance; if not it will fall back to class pay_rate
        else:
            return round(self.price * self.quantity,2)


    def change_price(self,price):

        assert price!=self.price, f"Updated price cannot be same as initial price!"

        self.price=price




    # A class method is a method that is bound to the class and takes the class itself as its first argument, commonly named cls. Class methods are used when the method needs access to the class itself but not necessarily to the instance. They can be used to create class-level operations or alternative constructors.
    @classmethod   # used to instantiate from any structured data like csv,yaml,json,etc
    def instantiate_csv(cls):
        with open ('items.csv','r') as f:
            #print(f.read())
            csv_reader = csv.DictReader(f)
            print(f"csv_reader= {csv_reader}")
            
            
            csv_list=list(csv_reader)
            
            for row in csv_list: #creating instnce for each row
                Item(
                    name=str(row.get('name')),
                    price=float(row['price']),
                    quantity=int(row['quantity']) 
                )
        
        print(f"{Item.discount_applicable}") # can access only class attributes
        # print(f"{Item.pay_rate}") # wont work because apply_discount() method is not been called yet
        # print(f"{self.price}") # cannot access self/instance arguments unless passed to this class method



    #Static methods are used when the method doesn't need access to the instance or its attributes. They are more like regular functions but are defined within the class for organization purposes.
    @staticmethod # method that is related to the class but not unique per instance
    def is_num_int(num):
        if isinstance(num,int):
            return True
        elif isinstance(num,float):
            return num.is_integer() #float() has a builtin function is_integer() which takes in float and works like => input-8.0 output-true(integer as .0);; input-8.8 output-false(float as .8)
        else:
            return f"Other" 
        
        print(self.price) # cannot access self/instance
        print(Item.pay_rate) # cannot access class 



    def __repr__(self): # magic method to represent objects the way we want them to be
        return f'{self.__class__.__name__}("{self.name}",{self.price},{self.quantity})'
    
    




if __name__ == '__main__':      # used so the below lines only execute when this file is run directly

    ## instantiating manually


    # Creating instances of class
    item1=Item('Earphones',269.76,55)
    item2=Item('Phone',13456.45,156)
    item3=Item('Laptop',34556.13,14)
    item4=Item('Watch',1322.46,15)
    item5=Item('TV',20076.89,7)



    print(f"################# Dictionary of Item class #################")
    print(Item.__dict__)
    print(f"################# Dictionary of item5 object #################")
    print(item5.__dict__)


    print('#'*100)
    print(f"item1.price = ${item1.price}")
    print(f"item2.price = {item2.quantity}")
    print(f"item3.price = {item3.name}")
    print(f"item4.price = ${item4.calculate_total_cost()}")

    print('#'*100)
    print(f"original_item5.total_cost = ${item5.calculate_total_cost()}")
    item5.apply_discount() #default value of 0.8 will be applicable here since no pay_rate has been passed
    print(f"item5.total_cost after 20% discount = ${item5.calculate_total_cost()}")


    print('#'*100)
    item6=Item("Tablet",17684.67)
    print(f"original_item6.total_cost = ${item6.calculate_total_cost()}")
    item6.apply_discount() #default value of 0.8 will be applicable here since no pay_rate has been passed
    print(f"item6.total_cost after {int(100-item6.pay_rate*100)}% discount = ${item6.calculate_total_cost()}")
    # item6.pay_rate=0.7
    item6.apply_discount(0.7) #pay_rate of 0.7 will be applicable here
    print(f"item6.total_cost after {int(100-item6.pay_rate*100)}% discount = ${item6.calculate_total_cost()}")

    print('#'*100)
    print(Item.all)







    print('#'*100)

    ## instantiating using csv

    #Calling the class method => instantiate_csv
    Item.instantiate_csv()

    print(Item.all)

    # Calling the static method => is_num_int
    print(Item.is_num_int('fhfb'))
    print(Item.is_num_int(10.0))
    print(Item.is_num_int(5))

    print(Item)


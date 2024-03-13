from oop_classmethod import Item  #importing all attributes inside oop_classmethod.py to the current file


class Phone(Item): # Phone class now inherts all the attributes from the Item class {parent_class => Item ;; child_class => Phone}

    # all=[]        # not needed as in parent class this will execute

    def __init__(self, name:str, price:float, quantity=1, broken_phones=0): # this takes input 
        
        assert broken_phones >=0 , f"No of broken_phones must be 0 or more!"

        self.broken_phones=broken_phones

        super().__init__(name, price, quantity) # this passes the input from the __init__ in the Phone class to __init__ in the Item class

        # Phone.all.append(self)        ## not needed as in parent class this will execute


    

phone1=Phone("s23ultra", 56000, 37)
phone1.broken_phones=9
phone2=Phone("15promax", 61000, 59)
phone2.broken_phones=13

print(phone1.calculate_total_cost())
phone2.apply_discount()
print(phone2.calculate_total_cost())

# print(Item.all)
print(Phone.all)



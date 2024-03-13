class Vehicle:

# polymorphism example
    
    def wheels(self):
        print(f"Vehicle has atlest 4 wheels")
        
    def fueltype(self):
        print(f"Vehicle uses Petrol or Diesel")

    def doors(self):
        print(f"Vehicle has atlest 2 doors")

    def drive(self):
        print(f"Vehicle is either fwd, rwd or awd")

    # method overloading
    def custom_fields(self, *args, **kwargs):
        print("arguments")
        print(args)
        print(f"keyword arguments")
        print(kwargs)

class Car(Vehicle):

    # method overriding
    def wheels(self):
        print(f"Car has 4 wheels")

    def fueltype(self):
        print(f"Car uses Petrol")

    def doors(self):
        print(f"Car has 4 doors")

    def drive(self):
        print(f"Car is fwd/rwd")


if __name__=='__main__':

    default_vehicle= Vehicle()

    default_vehicle.wheels()
    default_vehicle.fueltype()
    default_vehicle.doors()
    default_vehicle.drive()
    default_vehicle.custom_fields()

    print("#"*100)

    car1= Car()

    car1.wheels()
    car1.doors()
    car1.custom_fields(1,2,"all")

    print("#"*100)

    car2= Car()

    car2.drive()
    car2.fueltype()
    car2.custom_fields(name="abccc", age=19, adult=True)



    # len() is another example of polymorphism where if a string is passed it return the count of characters and if a list is passed it returns to no of items in the list.
    print("#"*100)

    name='Jane'
    print(len(name))

    listt=["James","Dow"]
    print(len(listt))

class Student:
    all=[]

    def __init__(self, name:str, marks:int):

        assert 0<=marks<=100, f"Marks must be between 0 and 100!"

        self.__name= name # by use __attribute_name we are creating a private attribute which cannot be accessed outside of the class
        self.marks= marks

        Student.all.append(self)

    # single or double __ do not enforce security and is a convention thing only where ---
    # single _ is used to let others know that the particular attribute is to be protected.
    # double __ is called as name mangling and the attribute can be still accessed/modified by using _classname.__attribute_name

    def get_grade(self) ->str : 

        if self.marks<35:
            return f"Fail"
        elif 35<=self.marks<70:
            return f"Average"
        elif 70<=self.marks<90:
            return f"Good"
        else: 
            return f"Excellent"



    # getter
    @property # using this decorater we define a read-only attribute. this behaves like a variable here
    def name(self):
        print('name property accessed')
        return self.__name

    # setter
    @name.setter # used to carry out some operations before storing the data like .upper()/.lower() or restricting character length etc.
    def name(self,new_name):
        print('@name.setter accessed')
        self.__name= new_name


    def __repr__(self):
        return f"Student_Name => '{self.name}' || Marks => {self.marks}"
    

student1=Student('James',59)
student2=Student('Dave',92)
student3=Student('Ava',70)
student4=Student('Eve',32)

print(student1.name)
print(student2.marks)
print(student3.get_grade())
print(student4.get_grade())

print("#"*100)
print(Student.all) 



# pripor to using __ and @property decorator anyone can easily change the attribute of the instance.
student3.name='Josie'
print(student3.name)

# now after using __ and @property decorator access is read_only and modifications are not possible
print(student3.name)
#print(student3.__name)  # __ cannot be accessed outside of the class unless setter is defined
student3.name='Nat'
student3.__name='Nat'


# but if we implement a @property.setter method we can now modify the attributes
student1.name='Jack'
print(student1.name)



# Enforcing strict privacy in Python is intentionally left to the developer's responsibility rather than being imposed by the language. This design philosophy is known as "we're all consenting adults here," and it emphasizes trust in the developer to follow conventions and best practices.


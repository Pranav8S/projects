#class and initialization

class student:

    def __init__(self, name, age, major, gpa, isLocal):

        self.name=name
        self.age=age
        self.major=major
        self.gpa=gpa
        self.isLocal=isLocal

    
    def has_distinction(self):
        if self.gpa > 7.0 :
            return True        
        else:
            return False
        

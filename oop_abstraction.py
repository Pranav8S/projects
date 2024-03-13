from abc import ABC, abstractmethod     # not necessary as even without this abstract methods can be implemented simply by extending parent class method

class email_setup:

    # abstraction example
    @abstractmethod
    def _email_validation(self):
        pass
    
    @abstractmethod
    def _smtp_initiation(self):
        pass

    @abstractmethod
    def _create_connection(self):
        pass

    def check_email(self,email):
        self.__email=email
        
        self._email_validation()
        self._smtp_initiation()
        self._create_connection()
    
        print(f"email {email} is being verified")


#creating instance
        
class my_email_checker(email_setup):


    #implementing the methods
    def _email_validation(self):
        print(f"email validation step")

    def _smtp_initiation(self):
        print(f"smtp initiation step")

    def _create_connection(self):
        print(f"connection creation step")


 
my_ec=my_email_checker()
my_ec.check_email('ashdvg@cnv.com')

 
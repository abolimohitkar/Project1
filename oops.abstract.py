from abc import ABC,abstractmethod
class RBI(ABC):
    @abstractmethod
    def add_data(self):
        pass
    
    @abstractmethod
    def sub_data(self):
        pass
    def create_data(self):
        a=10
        b=20
        x=a+b
        print(x)
        

    
class SBI(RBI):
    def add_data(self):
        print('the amount should not be less than 1000')
    
    def sub_data(self):

        print('data should be not less')
     
    


    

     
s1=SBI()
s1.add_data()
s1.sub_data()
s1.create_data()



class Student:
    institute='kiransir'
    n=int(input('enter the value:'))
    def __init__(self,nm,rl,mk):
        self.name=nm
        self.rollno=rl
        self.mark=mk
    def get_info(self):
        print(f'my name is {self.name}')    

    @classmethod
    def creadit(cls,x):
        x= x+(Student.n)
        print(f'my name is{cls.institute}')

    @classmethod
    def debit(cls,preamount):

        x=preamount+(Student.n)
        
        print(f'my marks are{x}') 


s1=Student('Ab',1,15)
print(s1.institute)
print(Student.institute)   
s1.get_info() 
s1.credit()   
s1.debit()


     
   

        
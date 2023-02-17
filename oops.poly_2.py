
# method Overriding:
class Vehicle:
    def __init__(self,nm,clr):
        print('Greatgrandparent class constructor')
        self.nm=nm
        self.clr=clr

    def Fourwheeler (self):
        x=('Maruti swift','Honda city','Wagnor','Jeep')
        print(f'I have  list of fourwheelers  {x}')  
    
class Car(Vehicle):
    def __init__(self,nm,clr,ag):
        print(' Parent1 and child class constructor')
        super().__init__(nm,clr)
        self.ag=ag
        print(f' I have {self.nm} car ,its colour is  {self.clr} and it is {self.ag} years old') 

    def Fourwheeler (self):
        super().Fourwheeler()
             
class Car1:
    def __init__(self,nm,clr,ag):
        print('parent2 class constructor')
        self.nm=nm
        self.clr=clr
        self.ag=ag
        print(f' i have {self.nm} car ,its colour is  {self.clr} and it is {self.ag} years old') 

    def Fourwheeler (self):
        x=('Maruti swift','Honda city','Wagnor','Audi')
        print(f'i have fourwheelers  {x}')  

class Car2(Car,Car1):
    def __init__(self,nm,clr,ag,avg):
        print('grandchild1 class constructor')
        super().__init__(nm,clr,ag)
        self.avg=avg
        #print(f' i have {self.nm} car ,its colour is  {self.clr} and it is {self.ag} years old, its avarge is {self.avg}') 

    def Fourwheeler (self):
        super().Fourwheeler()
              
class Newcar(Car):
    def __init__(self,nm,clr,ag,rt):
        print('child2 class constructor')
        super().__init__(nm,clr,ag)
        self.rt=rt
        #print(f' i have {self.nm} car ,its colour is  {self.clr} and it is {self.ag} years old and its rating is {self.rt}') 

    def Fourwheeler (self):
        super().Fourwheeler()

class Car3 (Car2):
    def __init__(self,nm,clr,ag,avg):
        print('greatgrandchild class constructor')
        super().__init__(nm,clr,ag,avg)
    
        #print(f' i have {self.nm} car ,its colour is  {self.clr} and it is {self.ag} years old, its avarge is {self.avg}') 

    def Fourwheeler (self):
        super().Fourwheeler()
              
d1=Car3('Mercedez','Black',15,15)
d1.Fourwheeler()
print(d1)
print(Car3.mro())         

# single inheritance:
''''
class Parent:
    def m1 (self):
        print(f'my property is my son')

class Son(Parent):
    def m2(self):
        print(f'my property is min and my father too')


p1=Son()  
p1.m1()
p1.m2()   
'''
#multilevel inheritance:
''''
class GraParent:
    def m1 (self):
        print(f'my property is my grandson')
class Parent(GraParent):
    def m2 (self):
        print(f'my property id my sons')
class Son (Parent):
    def m3(self):
        print(f'my property is mine and my father and my grandfathers')

agrim=Son() 
agrim.m1()
agrim.m2()
agrim.m3()                       
'''

#mutliple inheritance:
''''
class Parent1:
    def m1(self):
        print(f'my property is my son')
class Parent2:
    def m2 (self):
        print(f'my property is my son')
class Son(Parent1,Parent2):
    def m3(self):
        print(f'my property is my parents')  
jay=Son()
jay.m1()
jay.m2()
jay.m3() 
'''
#heriarchical inheritance:
''''
class Parent1:
    def m1(self):
        print(f'my property is my son1+son2')
class Son1(Parent1):
    def m2 (self):
        print(f'my property is my parent')
class Son(Parent1):
    def m3(self):
        print(f'my property is my parent')  
jay=Son()
jay1=Son1()

jay.m1()
jay.m3()
jay1.m1() 
jay1.m2()
'''


#hybrid inheritance:  
class A:
    def m1(self):
        print('I am Grandfather')
class B(A):
    def m2(self):
       
       print('I am son of A')      
class C:
    def m3(self):
       print('I am mother of D') 
class D(B,C):
    def m4(self):
       print('I am son of B and C and grandson ofA') 
class E(B):
    def m5 (Self):
       print('I am son of B') 
class F (D):
    def m6(self):
         print('I am son of D') 
jay=F()
jay.m2()
jay.m6()  
jay.m1()
jay.m3() 
viru=D()
viru.m1()
viru.m2()
viru.m3() 
ram=E() 
ram.m2()
ram.m1()
   


 


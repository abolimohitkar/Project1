#odd_even number
#n=int(input('enter the number:'))
#if n%2==0:
#    print('Number is even')
#elif n%2==1:
#   print('number is odd')
    
#else:
#    ('number is good')
''''
#factorial
def number():
    n=int(input('enter the number:'))
    for i in n:
        sum=1
        sum=i*sum
    print(i)
    return(sum)
    
    
number() 
'''
''''
a=15
b=15
c=15
if  a>b and a>c:
     print('a is max number')
elif b>c and b>a:
     print('b is max number') 
elif c>b and c>a:
     print('c is max number')
else:
    print('numbers are equal')        
'''
''''           
#minimum function    
a=15
b=25
c=15
if  a<b and a<c:
     print('a is min number')
elif b<c and b<a:
     print('b is min number') 
elif c<b and c<a:
     print('c is min number')
else:
    print('numbers are equal')  
'''
''''
x=10
x1=eval('x**2')
print(x1)
'''
#divisible by 3And 5 
''''    
n=15
if n%3==0:
    if n%5==0:
        print('its divisible by 3 and 5')
    else:
        print('its divisible by 3 only')
else:
    print('its  divisible by 5 only')    
'''
''''
# find the range
sum=0
for i in range(100,200):
    if i%2==0:
        sum=sum+i
        print(i)
''' 
''''      
# WAP to find the leap year
def leap_year():
    n=int(input('Enter the leap year:'))
    while True:
        if (n%4==0 and n%100!=0 or n%400==0):
            print('This is leap year',n)
        else:
            print('This is not leap year',n)
        return(n)
         
  
leap_year()  
'''
''''
def marksheet():
    a=int(input('enter the english marks:'))

    a1=int(input('enter the maths marks:'))

    a2=int(input('enter the science marks:'))

    a3=int(input('enter the socialscience marks:'))

    avg_marks=a+a1+a2+a3/4
    if avg_marks>=90:
        print('Distinction')
    elif  avg_marks<90 and avg_marks>60:
        print('First class')
    elif avg_marks <60 and avg_marks>50:
        print('second class')
    else:
        print('Fail')

marksheet()    
'''
''''
def marksheet():   
    d={1:['maths',18],2:['english',25],3:['sociascience',30]}
    print(d.keys())
    print(d.values())
    avg=(d[1][1]+d[2][1]+d[3][1])/3
    print(avg//1)
 
marksheet()    
'''
''''
print('we are in global')
x=15
y=20
def max():
    x=10
    y=20
    print(x,y)
    print('we are in loca scope')
    
    def min():
        x=15
        y=45
        print(x,y)
        print('we are superlocal')
        
    
        def xtramin():
            x=100
            y=200
            print(x,y)
            print('we arein extralocal')
            
        xtramin()  
    min()         
            
    
max()


print(x,y)
'''
''''    
print('we are in global')

def max(x,y,z):
    print(x,y,z)
    
    print('we are in loca scope')
    
    def min(x,y,z):
        
        print(x,y,z)
        print('we are superlocal')
        
    
        def xtramin(x,y,z):
            
            print(x,y,z)
            print('we arein extralocal')
            
        xtramin('agrim','pranit','bagdi')  
    min('pranit','omprakash','bagdi')         
            
    
max('aboli','pranit','bagdi')
'''
''''
print('we are in global')

def max(x='aboli',y='pranit',z='bagdi'):
    print(x,y,z)
    
    print('we are in loca scope')
    
    def min(x,y,z):
        
        print(x,y,z)
        print('we are superlocal')
        
    
        def xtramin(x,y,z):
            
            print(x,y,z)
            print('we arein extralocal')
            
        xtramin('agrim','pranit','bagdi')  
    min('pranit','omprakash','bagdi')         
            
    
max()
'''
''''
def values(*aboli):
    print(aboli)
    
    for i in aboli:
        s=s+i
    print(s)
        
        
values(1,2,3,4,5,6)        

def student(**kwargs):
    print(kwargs)
    t=0
    for k,v in kwargs:
        print(k,v)
        
    print(i)
     
student(n=1,n1=2,n3=3)       

''' 
''''
f=lambda a,b,c,d: c if a>b else d
v=f(45,2,3,4)
print(v)
'''
''''
n=int(input('enter the number:'))
if n>1:
    for i in (2,n):
        if (n%i==0):
            print('the number is not prime')
        else:
            print('its prime')
else:
    print('its prime')
'''


''''
n=8
for i in range(n+1,1,-1):
    for j in range(1,i-1):
        print( '*',end=" ")
    print() 
for i in range(1,n):
    for j in range(1,i):
        print('*',end=" ")
    print()
'''
''''
n=5
for i in range(1,n):
    for j in range(i-1,i):
        print('*',end='')
    print()
'''
x=[10,20]
y=x
print(y)
y+=[30,40]
print(y)
print(x)

         
    
    
    
    
    
    
     

        
       
        




   
        
    
       
       
       
     
    

    
        
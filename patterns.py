# ''''
# #revrese right angle triange
# n=5
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(' ',end=" ")
#     for j in range(i,n):
#         print( '*',end=" ")
#     print()    

# # Tree shape
# n=5
# for i in range(1,5):
#     for j in range(i,n):
#         print('',end=" ")
#     for j in range(1,i+1):
#         print( '*',end=" ")
#     print() 
# #reverse rightangle
# n=5
# for i in range(1,5):
#     for j in range(i+1):
#         print('',end=" ")
#     for j in range(i,n):
#         print( '*',end=" ")
#     print()    
# '''
# ''''
# ##
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end=" ")
#     for j in range(i,n):
#         print('*',end=" ")
#     print() 
    

# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for j in range(i+1):
#         print( '*',end=" ")
#     print()             
             
# #n=65
# for i in range(1,5):
#     for j in range(1,i):
#         print( chr(105),end=" ")
#     print()
# for i in range(6,1,-1):
#     for j in range(1,i-1):
#         print(chr(105),end=" ")
#     print()             
# '''
# ''''
# for i in range(0,5):
#     for j in range(0,5):
#         if j==1 or i==1 or i==3   :
#             print('*' ,end=" ")
#     print()        
# '''
# ''''
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 
# '''
# for i in range(1,1001):
#    num=i
#    sum1=0
#    n=len(str(i))
#    print(n)
#    ''''
#    while(num!=0):
#        digit=num%10
#        sum1=sum1+digit**n
#        num=num//10
#        if i==sum1:
#             print(i)
# 
#     '''
# n=1        
# for i in range(1,6):
#     for j in range(1,i):
#         print(n,end=' ')
#         n+=1
#     print('')    

#print('The {} side {1} {2}'.format('bright', 'of', 'life'))


#'{0}'.format(4.56) '{0}'.format([4.56,])
#-----------------------------------------------------------#
#pattern
# 1
# 33
# 555
# 7777
# 99999
# n=5
# k=n-1
# for i in range(0,6):
#     for j in range(0,i):       
#         print(i*2-1,end='')
#     print()
#------------------------------------------------------------#
#pattern-
# 55555
# 4444
# 333
# 22
# 1
# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(i,end='')
#     print()          
#--------------------------------------------------------------#
# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# ---->
# for i in range(1,7):
#     for j in range(1,i):
#         i-=1
#         print(i,end=' ')
#     print()
#------------------------------------------------------------------#
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1
# 2 1
# 1


# for i in range(6,0,-1):
#     for j in range(0,i-1):
#         i-=1
#         print(i,end=' ')
#     print()
#-----------------------------------------------------------------#
# 1  
# 3 2  
# 6 5 4
# 10 9 8 7
# x=1
# y=2
# z=y
# for i in range(2,6):
#     for j in range(1,i):
#         z-=1
#         print(z,end=' ')
# #     print(" ") 
#     x=y
#     y+=i
#     z=y   
#---------------------------------------------------------------------#
#           1 
#         1 2 
#       1 2 3
#     1 2 3 4
#   1 2 3 4 5
# rows = 6
# for i in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print("")
#-----------------------------------------------------------------------#
# 1   
# 2  4
# 3  6  9
# 4  8  12  16
# 5  10  15  20  25
# 6  12  18  24  30  36
# 7  14  21  28  35  42  49
# 8  16  24  32  40  48  56  64


# for i in range(1,9):
#     for j in range(1,i+1):
#         sq=i*j
#         print(i*j, end='  ')
#     print(" ")    
#------------------------------------------------------------------------------#
#         * * * * * * 
#          * * * * * 
#           * * * *
#            * * *
#             * *
#              *
# X = 5
# Y = 2 * X - 2
# for i in range(X, -1, -1):
#     for j in range(Y, 0, -1):
#         print(end=" ")
#     Y = Y + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")


#---------------------------------------------------------------------#
    #       *  
    #      * *  
    #     * * *
    #    * * * *
    #   * * * * *
    #  * * * * * * 

# n=6
# k= (2 * n) - 2    
# for i in range(0,n):
#     for j in range (0,k):
#         print(end=' ')
#     k=k-1   
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print(" ")
#-------------------------------------------------------------------------#
# def fname(**x):
#     print("my name is "+ x['f']+x['c'] )

# fname(f='aboli',c='jbk')  
#----------------------------------------------------------------#  
# def fun(n):
#     return lambda a:a*n 
# x=fun(2)
# print(x(11))
# ---------------------------------------------------------------#
# class aboli:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b 
#     def agrim(x):
#         print('my name is aboli'+x.a)
# p1=aboli('aboli','agrim')
# p1.agrim()
#----------------------------------------------------------------#
# class grandparent:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def parent(self):
#         print('my name is ',self.a)
# p1=grandparent('a','b')
# p1. parent() 
#----------------------------------------------------------------------#
# import datetime
# x=datetime.datetime.now()
# print(x.year) 
# print(x.strftime("%A"))   
#-----------------------------------------------------------------------#   
# import module
# x={'name':'aboli','age':30,'hight':5.2}

# x1=module.x['name']
# print(x1)
#--------------------------------------------------------------------------#
# import json


# x='{"name":"aboli","age":30,"marks":45}'    
# x1=json.loads(x)
# print(x1)
#-------------------------------------------------------------------------#
# n=5
# for i in range(1,6):
#     for j in range(1,i+1):
#         if j==2:
#             print('*',end=' ')
#         else:
#             print(j,end=' ')    
        
#     print()    
#-------------------------------------------------------------------------#
# s='python'
# for i in range(len(s)):
#     for j in range(0,i+1):
#         print(s[j],end=' ')
#     print() 
# --------------------------------------------------------------------------------
# a=10
# b=20
# #b,a=10,20
# # print('value of b--->',b)
# # print('value of a--->',a) 
# temp=0
# a=a+temp
# print(a)
# b=a
# print(b)
# b=b+a
# print(b)

# s='agrim'
# print(s[ ::-1])

# s='aboli bagdi'
# x=s.split()
# # print(x)
# # print(x[0][ : :-1],x[1][ : :-1])
# l=[]
# for i in x:
#     l.append(i[ : :-1])
#     z=' '.join(l)
#     print(z)

# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(i,end=' ')
#     print()  

# n=int(input('enter the number:'))
# print([i if n%2==0 else"number is invalid"])
#-----------------------------------------------------------------------
# n=int(input('enter the number:'))
# for i in range(2,n):

#     if n%i==0:
#         print(i,'it is not prime')
    
#     else:
#         print(i,'it is prime')
#-----------------------------------------------------------------------
# #n=int(input("enter the number:"))
# for i in range(1,1001):
#     num=i
#     sum=0
#     n=len(str(i))
#     while(num!=0):
#        digit=num%10
#        sum=sum+digit**n    
#        num=num//10     
#     if i==sum:
#         print(i)

# n=int(input('enter the number:'))
# s=0
# i=n
# print(n)
# z=len(str(i))
# print(z)
# while(n!=0):
#     a=n%10
#     print(a)
#     s=s+a**z
#     print(s)
#     n=n//10
#     print(n)
#     if i==s:
#        print('number is armstong')
#     else:
#        print('number is not armstong') 
#   
# n=int(input('enter the number:'))
# first=0
# second=1
# for i in range(0,n):
#     print(first,end=" ")
#     temp=first
#     first=second
#     second=temp+first

# n=input('entre the string:')
# rev_string=n[ : : -1]
# if n==rev_string:
#     print('its palindrome')
# else:
#     print('its not')    
# s=input('enter the string:')
# print('oringinal string:'+s)
# rname=""
# for char in s:
#     rname=char+rname
# print('reverse string-->'+ rname)

# s='I AM ABOLI from pune'
# z=s.split()
# y=[]
# for i in z:
#     x=i[ : :-1]
#     y.append(x)
#     q='  '.join(y)
#     print(q)
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2
# 1

# for i in range(5):
#     for j in range(1,6-i):
#         print(j,end=" ")
#     print()        
    
# for i in range(5,0,-1): 

#     for j in range(0,i):
#         print(i,end=" ")
#     print()

# l1=[1,2,3]
# list=[x//2 for x in l1]   
# print(list)      

# list=[2,3,5,6, 7,8]
# l1=[x%2 for x in list]
# print(l1)


# n=int(input('enter the number:'))

# #print([i for i in range(n)if i%3==0 if i%2==0])

# print([i if i%3  ==0 else "invalid" for i in range(n)])
# l=[1,2,3,4,3,3,5]
# l1=[]
# for i in range (len(l)):
#     if l[i]==3:
#         l1.append(i)
# print(l1)

# s=' i learn python and python is popular'

# #d={"i":1,'learn':1..........}
# d={}
# x=s.split()
# for i in x:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)            
        

# n=input('enter the value:')
# s='A,E,I,O,U,a,e,i,o,u'
# #for i in s:
# if n in s:
#     print('the number is vowels')  
# else:
#     print('the value is cosonents')          

# l=['name','aboli','mohit']
# l1=[1,2,3]
# z=zip(l,l1)
# print(dict(z))
# for i in z:
#     print(i)
#     z=list[z]
#     print(z)

# z=2**3**2 it willcalculate value from rightto left
# print(z)
        
# def display():
#     return ('hello')
# def myfun(fun):
#     print(fun())
# print(myfun(display))  
# 
      
# n=7
# s=(n  * 2) -2
# for i in range(0,n):
#     for j in range(0,s):
#         print(end=' ')
#     s=s-1    
#     for j in range(0,i+1):
#         print('*',end=' ')    
#     print( )  
    
        
# # n=6
# # k= (2 * n) - 2    
# # for i in range(0,n):
# #     for j in range (0,k):
# #         print(end=' ')
# #     k=k-1   
# #     for j in range(0,i+1):
# #         print('*',end=' ')
# # #     print( )
# n=1
# m=2
# q=m
# for i in range(1,6):
#     for j in range(n,m):
#         q-=1  
#         print(q,end='  ')
#     print(  ) 
#     n=m
#     m+=i
#     q=m  


# input
# l = [10, 5, 7, 4, 3, 11, 10]

# #output:[10, 'five', 7 , 'Four', ]

# for i in range (0,4):
#     if (l[i]==5):
#         l.remove(5)
#         l.insert(1,'five')
#     elif(l[i]==4):
#         l.remove(4)
#         l.insert(4,'four')    
# print(l)  

# #a=(1,2,3,4)

# l=list(a)
# l.append(50)
# print(l)
# a=tuple(l)
# print(a)


# #out=[1,2,5]
# l=[]
# len_a=len(a)
# for i in range(len_a):
#     if a[i]<6:
#       l.append(a[i])
# print()
# l[1]=2
# print(l)    

''''
for i in range (0,6):
   
    if (a[i]==3):
        a.remove(3)
        a.insert(1,2)   
        print(a[0 :3])
'''        
       
# a =[1,3,5,9,8,7,11]
# l=[]
# for i in range(len(a)):
#     print(a[i]) 
#     if a[i]==5:  
#         l.append(i)
#         break



# a=lambda x,y:(x+y,x-y)  
# z,e=a(10,20)
# print(z)
# print(e)
# t=(10,20)
# v=0
# l=[]
# if t or v and l:
#     print('true')
# else:
#     print('false') 
# print(R"hello\namol") 

# print rahul 100 times:

# def aboli(x):
#     return x*100
# z=aboli('rahul')
# print(z)


# #Quest:   
# def pattern(n):
#     for i in n:
#         print('|',end=' ')
#         print('*'* int(i),end='  ')
#     print()        
# n='3456'
# pattern(n)       


n=int(input('enter the value'))
s=1
for i in range(1,n):
    if n%i==0:
        s=s+i
        print(i, '--->   the number is perfect')
        
    else: 
        print('number is not perfect')
        


    







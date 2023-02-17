#Armstong Number:
# for i in range(1,1001):    
#     num=i
#     sum1=0
#     n=len(str(i))
    
#     while(num!=0):
#         digit=num%10     #1%10
#         sum1=sum1+digit**n    #0+0.01**3
#         num=num//10    #1//10

#     if i==sum1:
#         print(i)
# #--------------------------------------------------------------------------

num =int(input("enter a number:"))
sum1=0
i=num
n=len(str(i))
print(n)
while(num!=0): 
    digit=num%10 #121%10
    print(digit)
    sum1=sum1+digit**n #121%10**
    print(sum1)
    num=num//10
    print(num)
if i==sum1:
    print("it is armstrong number")
else:
     print("not an armstrong number" )   
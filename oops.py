class Bank:
    def __init__(self):
        self.__amount=500
  
    def credit(self,n):
        x=int(input('enter the value:'))    
        n=self.__amount+n
        if x>0:
           print(n)
        else:
            print('Amount is negative')   
    def debit():
            x1=int(input('enter the value:'))
            amount-=amount
            if amount>=1000:
                  print(' your balance is ',amount)
                  
            elif amount==0:
                  print('You  can not widrow  total amount,minimum balance is  Rs.1000rs')

            else:
                print('Wrong amount is entered')            
        
    

s1=Bank()
s1.credit(500)



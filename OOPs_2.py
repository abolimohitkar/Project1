class SBI:
      
      
      def __init__(self,nm,acc,acctype,bl):
           self.name=nm
           self.account=acc
           self.account_type=acctype
           self.balance=bl
      
      def creadit(self,n):
            amnt=int(input('enter the value:'))    
            amnt=n+amnt
            if amnt>0:
               print(amnt)
            else:
               print('Amount is negative')   

      def debit(self,pramt):
            
            amnt=int(input('enter the value:'))
            amount=pramt-amnt
            if amount>=1000:
                  print(' your balance is ',amount)
                  
            elif amount==0:
                  print('You  can not widrow  total amount,minimum balance is  Rs.1000rs')

            else:
                print('Wrong amount is entered')            

                
      def transfer_otherbankacc(self,blc):
            s2.balance=s2.balance+blc
            print(s2.balance)

s1=SBI('aboli',101101,'saving',15000) 
print(s1.balance)
s2= SBI('Agrim',101102,'saving',12000) 
print(f'my {s1.name} having accountno {s1.account} is {s1.account_type}and balance is{s1.balance}') 
print(f'my {s2.name} having accountno {s2.account} is {s2.account_type}and balance is{s2.balance}')       
s1.creadit(1000)
s1.debit(15000)
s1.transfer_otherbankacc(15000) 
s2.transfer_otherbankacc(12000)   
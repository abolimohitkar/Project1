
def menucard():
  x= {1:['Tea',10,1],2:['coffee',20,2],3:['vadapav',10,3],4:['bhel',30,4],5:['Idli',30,5]}
  print ("hello!,welcome to AGRIM'S CAFE")
  print('--'*40)
  print('''  MENUCARD
             1:Tea         2:samosa     5.Idli
             3:vadapav     4.Bhel
          ''')
  print('--'*40)
l=[]
while True:
  menucard()
  ch=int(input('enter your option:'))
  q=int(input('enter the quantity:'))
  t=(ch,q)
  l.append(t)
    
choice= input('do you want to continue y/n:')

if choice== 'n':

   print(l)
   
   
      
print('--'*60)
print('sr.no     \t|item    \t|amount   \t|quanity  \t|total amount')
print('--'*60)

s=0
    
for i in l:
         print( x[i[0]][2],'\t\t|',x[i[0]][0],  '\t\t|',x[i[0]][1],  '\t\t|',i[1] ,'\t\t|',x[i[0]][1]*i[1])
         s=s+x[i[0]][1]*i[1]
         v=s*float(0.05)
         v=v//1+s
         
print('--'*60)   
print('Total amount of bill is  with GST:',v,'/-')
      
print('Thank you ..')
print('--'*60)
   
        
               


    
# sum using define
''''
def  sum():
    a=10
    b=20
    a=a+b
    a=a*b
    b+=a
    print(a,b)
    return(a,b)
sum()
'''

      
''''
class Timing(Exception):

    def __init__(self,msg):
        self.msg=msg
    
try: 
    n=int(input('enter the timing:'))
    if n>9:
        print('print you are late')

    elif n<=9:
        print('you are on time')

    else:
        print('you are not late')
        

except Exception as e:
    print('you are late')
    print(e)

finally:
    print('Office time is 9.00am')
'''
''''

try:
    print(x)
except NameError:
    print('variable x is not defined')
except:
    print('somethingwent wrong')    
'''
''''
try:
    print('hello')
except:
    print('something went wrong')
else:
    print('nothing went wrong')   

finally:
    print('try except and finish')
'''
''''
x= 'hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed')
'''

grocerry=('i have to groerry list {item} and {quantity}')

print(grocerry.format(item='poha',quantity='10kg'))
item='poha'
name='10'
print(f'i have {item} and its name{name}')

    


    

    

   


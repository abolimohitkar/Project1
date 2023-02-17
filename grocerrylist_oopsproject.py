db=[]

class Grocerry:
    def __init__(self,sr,itm,qunt,unit):
        self.srno=sr
        self.item=itm
        self.quantity=qunt
        self.unit=unit

    def __str__(self):
        return self.item 
               

    def create_list(self):
        sr_no=int(input('enter the number:'))
        item_name=input('enter the name:')
        item_quantity=int(input('enter the quanity:'))
        item_unit=input('enter the unit:')
        g1=Grocerry(sr_no,item_name,item_quantity,item_unit)
        db.append(g1)
        print('record is placed in db')
        


    def display_list(self):
        print('--'*60)
        print('sr.no','\t\t|','item','\t\t|','quantity','\t\t|','unit')
        print('--'*60)

        for i in range(len(db)):
            print('--'*60)
            print(db[i].srno,'\t\t|',db[i].item,'\t\t|',db[i].quantity,'\t\t|',db[i].unit)
            print('--'*60)

    def search_item(self):
        sr=(input('enter the number:'))
        for i in range(len(db)):
            if db[i].item == sr:
                print(db[i])
                return db[i]   
    def delete_item():
        sr=(input('enter the number:'))
        for i in range(len(db)):
            if db[i].item == sr:
                del i
                

             


s1=Grocerry(0,' ',0,' ')
#s2=Grocerry(1,'poha',5,'kg')
#s3=Grocerry(2,'sakhar',5,'kg')
#db.append(s2)
#db.append(s3)
#print(s2,s3)

def screen():
    print('''
        1)Create list
        2)Display list
        3)Update list
        4)delete item from list
        5)search item from list
        ''')


while True:
    screen()
    option=int(input('enter the number:'))
    
    if option==1:
        s1.create_list()
     
    elif option==2:
        if len(db)!=0:
            s1.display_list()
        else:
            print('data is not found')

    elif option==3:
        pass
    elif option==4:
        s1.delete_item()
    elif option==5:
        i=s1.search_item()
        if i in db:
            print('data is found')
        else:
            print('data is not found')

    else:
        print('invalid option')

    ch=input('Do you want to continue y/n:')
    if ch.lower()!='y':
    
        break    


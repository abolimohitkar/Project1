
db=[]
class Student:
    def __init__(self,nm,rl,mk):
        self.name=nm
        self.rollno=rl
        self.mark=mk
    def __str__(self):
        return self.name

    def create_data (self):
        n=input("enter the name:")
        rl=eval(input('enter the rollno:'))
        mk= eval(input('enter the marks:'))
        x=Student(n,rl,mk)
        db.append(x)
        print('record is placed in database')

    def read_data (self):
        print('--'*40)
        print('sr.no',('\t\t'),'rollno',('\t\t'),'mark')
        print('--'*40)
        for i in range(len(db)):
            print('--'*40)
            print(db[i].rollno,'\t\t|',db[i].name ,'\t\t|',db[i].mark)
            print('--'*40)



s1=Student('jay',1,2)
#db.append(s1.mark) 
print(db)
dummyobject=Student( " ",0,0)



def form():

    print('''
           1) Create data of student
           2) Display data of student
           3) update data of student
           4) Delete data of student

           '''
    )
while True:
    form()
    choice=int(input("Enter the number:"))

    if choice==1:
        dummyobject.create_data()   
    elif choice==2:
            dummyobject.read_data() 


    elif choice==3:
        pass
    elif choice==4:
        pass
    else:
        print('enter valid number')

    ch=input('Do you want to continue y/n:')

    if ch.lower() != "y" :
       # for i in db:
        #    print(i) 
        break 
        
        









db={1:{'name':'Aboli M','std':'5th','event':"Singing",'rollno':1},
    2:{'name':'Amit','std':'6th','event':"Dancing",'rollno':2},
    3:{'name':'Aradhya','std':'6th','event':"Drama",'rollno':3},
    4:{'name':'Akshay','std':'6th','event':"Dancing",'rollno':4},
    5:{'name':'Ajay','std':'6th','event':"Drama",'rollno':5},
    6:{'name':'Vijay','std':'6th','event':"Quize",'rollno':6},
    7:{'name':'Aisharya','std':'6th','event':"Dancing",'rollno':7},
    8:{'name':'Adinath','std':'5th','event':"Singing",'rollno':8},
    9:{'name':'Priyanka','std':'6th','event':"Quize",'rollno':9},
    }
def dashboard():
    print('Welcome to  RKL Student  Event Managment System ')
    print('''
          Event
          
          1)Create a List of Students
          2)Display List of Students
          3)Update data from List
          4)Delete Details
          5)Students by events
          
          
         ''' )
    
def create():
    rno=int(input('Enter the Roll Number:'))
    name=eval(input('Enter the name:'))
    std=input('Enter the Std:')
    event=eval(input('Enter the event:'))
    print(f'The Roll no{rno} details are filled successfully')
    small_dict={}
    small_dict['name']= name
    small_dict['std']= std
    small_dict['event']= event
    small_dict['rollno']=rno
    print(small_dict)
     
    db[rno]=small_dict
    #print(db)    

def display():
    
    #print('*'*80)
    #print('sr.No',('\t\t'),'Name',('\t\t'),'std',('\t\t'),'Event',('\t\t'),'rollno')
    #print('*'*80)
    #for i in (db.keys()):
        
    #   print(i,('\t\t|'),db[i]['name'],('\t\t|'),  db[i]['std'],  ('\t\t|'),  db[i]['Event'],('\t\t|'),db[i]['rollno'])
    
    if len(db)!=0:
        print('-'*60)
        print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn='ROLLNO',n='NAME',s='STD',e='EVENT'))
        print('-'*60)
        for i in db.values():
           print('-'*60) 
           print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn=i['rollno'],n=i['name'],s=i['std'],e=i['event']))
           print('-'*60) 
    else :
        print('empty')
    print('-'*60)        
       
def update():
    if len(db)!=0:
        rollno= eval(input('enter the  rollno to update its record:'))
        if rollno in db:
           name=eval(input('enter the name:'))
           std=(input('enter the std:'))   
           event=eval(input('enter the event:')) 
           
           db[rollno]['name']=name
           db[rollno]['std']=std
           db[rollno]['event']=event
        
           print('Student data is updated successfully')
        else:
            print('no record is updated')
    else:
        print('no data base found')        
              
    
    
def delete ():
    if len(db)!=0:
        rollno=eval(input(' Enter the student rollno to delete data from memory:'))
        if rollno in (db):
            del db[rollno]
            
        else:
            print ('No student  roll no is found in db. pls enter correct rollno')
    else:
            print('no record is dispay')  
            
def search ():
    l=[]
    print('''
            1)Singing
            2) Dancing
            3)Quize 
            4)Drama
         ''')   
       
    chc=input('enter the choice:') 
    if chc==1:
        for k ,v  in db.items():
            if v['event']=='Singing':
                l.append(k)
                print('__'*60)
                print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn='rolln',n='name',s='std',e='event'))
                print('__'*60)     
                
                for i in l:
                    print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn=db[i]['rollno'],n=db[i]['name'],s=db[i]['std'],e=db[i]['event']))    
    elif chc==2:  
            print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn=db[i]['rollno'],n=db[i]['name'],s=db[i]['std'],e=db[i]['event']))                                    
    elif chc==3:  
            print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn=db[i]['rollno'],n=db[i]['name'],s=db[i]['std'],e=db[i]['event']))     
    elif chc==4:  
            print('|{rn:^15}|{n:^15}|{s:^15}|{e:^15}'.format(rn=db[i]['rollno'],n=db[i]['name'],s=db[i]['std'],e=db[i]['event']))         
               #print(f'(Total number of student participated in Singing competion {a},and Dancing cometiotion {b}')                      
while True:    
    dashboard()
    choice=int(input('enter choice:'))

    print(choice)
    
    if choice==1:
        create()
    elif choice==2: 
        display()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        search()    
    else:
        print('invalid choice')
        
    
    ch=input('do you ant to continue y/n:')
    
    if ch.lower()!='y':
        print(db) 
        break    


     
    
    
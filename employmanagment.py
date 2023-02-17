
db={101:{'name':'Aboli Mohitkar','dep':'HR','salary':25000,'U_id':101},
    102:{'name':'Agrim','dep':'Admin','salary':25000,'u_id':102},
    103:{'name':'Aradhya','dep':'IT','salary':85000,'u_id':103},
    104:{'name':'Akshay','dep':'Sweeper','salary':8000,'u_id':104},
    105:{'name':'Ajay','dep':'Watchman','salary':15000,'u_id':105},
    106:{'name':'Aajay','dep':'Helper','salary':12000,'u_id':106},
    107:{'name':'Aisharya','dep':'Manager','salary':125000,'u_id':107}}
def dashboard():
    print('Welcome to Bank Salary Account Managment System ')
    print('''
          Menu
          1) Creat record of Employee
          2)Display of employee
          3)Udate Employee
          4)Delete Employee
          5) Search Employee having salary below 15000
          
          
         ''' )
    
def create():
    u_id=int(input('Enter the ID:'))
    name=input('Enter the name:')
    dep=input('Enter the dep:')
    salary=eval(input('Enter the salary:'))
    print(f'The{u_id} details are filled successfully')
    small_dict={}
    small_dict['name']= name
    small_dict['dep']= dep
    small_dict['salary']= salary
    small_dict['u_id']=u_id
    print(small_dict)
     
    db[u_id]=small_dict
    print(db)     

def display():
    
    print('*'*60)
    print('*'*60)
    for i in (db.keys()):
        
       print(i,'\t\t|',db[i]['name'],'\t\t|',db[i]['dep'],'\t\t|',db[i]['salary'])
    #if len(db)!=0:
    #    print('-'*60)
#        print('|{id:^15}|{n:^15}|{d:^15}|{s:^15}'.format(id=i['u_id'],n=i['name'],d=i['dep'],s=i['salary']))
    print('*'*60)        
       
def update():
    if len(db)!=0:
        u_id= eval(input('enter the id  to update its record:'))
        if u_id in db:
           name=eval(input('enter the name:'))
           dep=eval(input('enter the dept:'))   
           salary=int(input('enter the salary:')) 
           
           db[u_id]['name']=name
           db[u_id]['dep']=dep
           db[u_id]['salary']=salary
        
           print('employee date is updated successfully')
        else:
            print('no record is updated')
    else:
        print('no data base found')        
              
    
    
def delete ():
    if len(db)!=0:
        u_id=eval(input(' Enter the employee u-id  to delete data from memory'))
        if u_id in (db):
            del db[u_id]
            
        else:
            print ('No id id found in db. pls enter correct id')
    else:
        print('no record is dispay')  
def search ():
  
    for i in db.keys():
        x=db[i]['salary']
        print('__'*60)
        print('|{u_id:^15}|{n:^15}|{d:^15}|{s:^15}'.format(u_id='u_id',n='name',d='dep',s='salary'))
       
        if x<25000 and x>=5000:
            
            print('|{u_id:^15}|{n:^15}|{d:^15}|{s:^15}'.format(u_id=db[i]['u_id'],n=db[i]['name'],d=db[i]['dep'],s=db[i]['salary']))
        elif x>=25000 and x<=50000:
            
            print('|{u_id:^15}|{n:^15}|{d:^15}|{s:^15}'.format(u_id=db[i]['u_id'],n=db[i]['name'],d=db[i]['dep'],s=db[i]['salary']))                                    
                          
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


     
    
    
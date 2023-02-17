def outer_fuc():
    y=50
    print('we are out,local scope')
    def inner_func():
            print('we are in inner func,locals scope')
            return double_inner
            def double_inner():
                print('123')
            double_inner()    
            
    print('in inner')       
    inner_func()       
    return y, inner_func      
            
        
print('we are calling sope')        
inner_fuc=outer_fuc() 
print(a)
double_inner=inner_fuc()

class Book:
    def __init__ (self,nm,authr,pg):
          self.name=nm
          self.author=authr
          self.page=pg

    def __add__(self,other):
         return self.page+other.page
               
    def __sub__(self,other):
         return self.page-other.page
  
  
    
              

b= Book('book','ab',450)
b1=Book('book1','ag',120)
print(f' addition of pages {b1+b}')
print(f' substration of pages {b-b1}')
print(f' Division of pages {b/b1}')





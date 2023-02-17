''''
with open('data.txt','r') as fd,open('data1.txt','a') as sd:
 x1=fd.read()
 sd.write(x1)
 print(x1)
 fd.close()
 '''


sd=open('data1.txt','r')
x1=sd.read(1)
print(x1)
fd=open('data.txt','w')
x=fd.write(x1)
print(x)


















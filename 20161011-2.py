for i in range(1,5,2):
 print(i)
print(list(range(1,5)))
x = ["SKKU", "University"]
for i in x:
 print(i)

for j in range(2,10,2):
 for i in range(1,10):
    print('{} * {} = {}'. format(j,i,j*i))
 print ("=" * 50)

i= int(input('시작단수 :'))
j= int(input('끝단수 :'))
for x in range(i,j+1):
 for y in range(1,10):
    print('{} * {} = {}'. format(x,y,x*y))
 print ("=" * 50)


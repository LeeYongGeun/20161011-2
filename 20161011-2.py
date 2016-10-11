start = 0
end = 0
while True:
    ans = input("x-y:")
    ran = ans.split('-')
    if len(ran) < 2:
        continue
    if int(ran[0]) > int(ran[1]):
        continue
    if ran[0].isdigit() and ran[1].isdigit():
        start = int(ran[0])
        end = int(ran[1])
        break
for i in range(start, end + 1):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))


def say():
    print('Hi')


say()  # 서브루틴보다 함수를 사용하기를 권장


def f(a, b):
    temp = 0
    if a >= b:
        temp = a
    else:
        temp = b
    return temp #함수안에서만 로컬변수로존재, return은 함수값을 보냄
print (f(1,2))
x= 50
def A(x):   # 함수밖에서 변수를가져올수없기에 input지정필요
    print(x)
    x = 2
    print(x)
A(x)
print(x)
print("="*50)
y= 50
def A():
    global y  # global 함수사용시 함수밖의 변수와 연동됨 def A() 비워놓을수있음
    print(y)
    y = 2
    print(y)
A()
print(y)

def func(a, b=5, c=10):
    '''Hi'''
    print ('a=',a ,'b=',b ,'c=', c)
func(1,3)
func(1, c=3)\
print(func(1).__doc__)
def func():
    pass #아무런 효과없음, 함수짤때자리 미리잡아놓을때용도
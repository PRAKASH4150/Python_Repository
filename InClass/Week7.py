import time
import calendar as cal
def squ(x):
    return x*x
myList=[1,2,3,4,5]

def myFunc1(*args):
    print(type(args))
    val="This is a composite string:"
    for arg in args:
        val+=arg
    
    return val
def myFunc2(**kwargs):
    val="This is a composite string:"
    for key,value in kwargs.items():
        val+=value
    
    return val



print(myFunc1('a','b','c'))
myDict={'1':'a','2':'b','3':'c'}
#print(myFunc2(myDict))

print(list(map(squ,myList)))

print((lambda x:x**2)(10))
cube=lambda x:x**3
print(cube(3))

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(cal.month(2024,6))


def myFunc(x):
    x=x+10

x=10
myFunc(x)
print(x)

print(*myList)

myIter =iter(myList)
print(next(myIter))
print(next(myIter))
print(next(myIter))

def nSqr(number):
	for i in range(number):
		yield i**2
for number in nSqr(5):
	print(number)

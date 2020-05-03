def A(a,b=30,c=5):
    print("함수 A입니다.")
    print("a와 b를 더한 값은 %d" %(a+b))

A(10,c=5)

def printTest(value, end="\n"):
              print(value+end+"홍길동")


printTest("zzdf",end =" zz")

def hello(*value):
    print(value)


List = (1,2,3,4,5)

hello(List)
hello(1,2,3,4,5,6)

tupleT = 1,2,3
a,b,c = tupleT
print(tupleT)
print(b)

def dicTest(**value):
    return value

test = dicTest(a=1,b=2)
print(test)


def status(name, age, isMan=True):
    print(name)
    print(age)
    if isMan:
        print("남자")
    else:
        print("여자")

status("김", 50)
status("홍",20,False)

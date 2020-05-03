class Test:
    num=30
    def show(self):
        print('num:'+str(self.num))
        print(str(self.array_num))
    def __init__(self):
        print("테스트 클래스에 오신걸 환영합니다.")
        
        self.num=20
        self.array_num=["ok"]
    def array_add(self, n):
        self.array_num.append(n)

t1 = Test()
t1.show()

t2 = Test()
t2.num=50
t2.show()

t1.show()

t1.array_add(1)
t2.array_add(3)

t1.show()
t2.show()

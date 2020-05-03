class Cal:
    result=0
    
    def plus(self,num1,num2):
        self.result = num1+num2
    def minus(self,num1,num2):
        self.result = num1-num2
    def mul(self,num1,num2):
        self.result = num1*num2
    def div(self,num1,num2):
        self.result = num1/num2
    def rem(self,num1,num2):
        self.result = num1%num2

c1 = Cal()

c1.plus(3,5)
c1.minus(5,3)
c1.mul(6,3)
c1.div(6,3)
c1.rem(5,3)
print(c1.result)

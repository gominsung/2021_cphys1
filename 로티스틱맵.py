class logic:
    def __init__(self,r,f_0):
        self.r=r
        self.f_0=f_0
        

    def homework(self):
        a=0
        for i in range(1,11):
            a=a+1
            f=self.r*self.f_0*(1-self.f_0)
            b="r=%f,n=%d일 경우의 함수값: %f" %(self.r,a,f)
            print(b)
            self.f_0=f



    def logiscal(self):
        self.r=float(input("r을 입력해 주세요: "))
        self.f_0= float(input("초기조건 f0를 입력해주세요: "))

        a=0
        while True:    
            for i in range(1,11):
                a=a+1
                f=self.r*self.f_0*(1-self.f_0)
                b="r=%f,n=%d일 경우의 함수값: %f" %(self.r,a,f)
                print(b)
                self.f_0=f
            repeat=input("계속 하시겠습니까? y/n: ")
            if repeat=="n":
                break
            else :
                self.r=float(input("r을 입력해 주세요: "))
                self.f_0= float(input("초기조건 f0를 입력해주세요: "))
                a=0

c=logic(0.5,0.5)
c.homework()
c=logic(2.5,0.5)
c.homework()
c=logic(4.5,0.5)
c.homework() 
c=logic(4.5,0.51)
c.homework()

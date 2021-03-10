r=float(input("r을 입력해 주세요: "))
f_0= float(input("초기조건 f0를 입력해주세요: "))

a=0
while True:    
    for i in range(1,11):
        a=a+1
        f=r*f_0*(1-f_0)
        b="r=%f,n=%d일 경우의 함수값: %f" %(r,a, f)
        print(b)
        f_0=f
    repeat=input("계속 하시겠습니까? y/n: ")
    if repeat=="n":
        break
    else :
        r=float(input("r을 입력해 주세요: "))
        f_0= float(input("초기조건 f0를 입력해주세요: "))
        a=0

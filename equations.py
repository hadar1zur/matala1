# -*- coding: utf-8 -*-
def exponent (x:float):
    num_total=0
    for i in range(0,100):
        num1=1
        num2=1
        for q in range(0,i):
            num1=num1*x
        for j in range(1,i+1):
            num2=num2*j
        num_total=num_total+(num1/num2)
    return(num_total)

def ln (x:float):
    if x<=0:
        return 0.0
    num_chek=x-1.0
    num_lan=num_chek+2*((x-exponent(num_chek))/(x+exponent(num_chek)))
    while (num_chek-num_lan > 0.001) or (num_lan > num_chek > 0.001) :
        num_chek=num_lan
        num_lan=num_lan+2*((x-exponent(num_lan))/(x+exponent(num_lan)))
    return(num_lan)
    
def XtimesY (x:float, y:float):
    ans=exponent(y*ln(x))
    if x<=0:
        return(0.0)
    return(ans)

def sqrt (x:float, y:float):
    ans=XtimesY(y, 1/x)
    return(ans)
   
def calculate (x:float):
    if x==0:
        return(0.0)
    ans=exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x, x)
    ans=float('%0.6f'% ans)
    return(ans)



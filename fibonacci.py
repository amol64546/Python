# 0 1 1 2 3 5 8 13 21 ....

def upto_n(num):
    f1,f2 = 0,1
    f3 = 1
    print(f1,f2, end=" ") 
    while f3<=num:
        print(f3, end=" ")   
        f3 = f1 + f2
        f1 = f2
        f2 = f3 
    


def nterms(num):
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")  
    

def nth(num):
    f1=0
    f2=1
    f3=1
    for i in range(2,num+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3    
    return f3

def rec(num):
    if num<2:
        return num
    return rec(num-1) + rec(num-2)

print(nterms(5))
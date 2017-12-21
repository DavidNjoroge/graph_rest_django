#!usr/bin/env python3.6

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

# print(fact(6))
prod=5895
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
for i in range(14):
    a=fib(i)*fib(i+1)
    if a==prod:
        print([fib(i),fib(i+1),True])
    elif a>prod:
        print([fib(i),fib(i+1),False])
        break
    

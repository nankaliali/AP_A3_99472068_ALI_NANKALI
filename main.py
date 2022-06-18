
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact


def sinus(n):
    sin = 0
    def inner(x):
        nonlocal sin
        for i in range(n):
            sin += (((-1)**i) * (((x*3.14)/180)**(2*i + 1)))/(factorial(2*i+1))
            #print(f'i = {i}  sin = {(((x*3.14)/180)**(2*i + 1))} / {factorial(2*i+1)} = {sin:.6f}')



        print(f'{sin:.6f}')
    return inner

n, x = input().split()
n = int(n)
x = float(x)
sin_ = sinus(n)
sin_(x)
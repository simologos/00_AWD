def fib_formula(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    val = (golden_ratio**n - (1 - golden_ratio)**n) / math.sqrt(5)
    return int(round(val))

def fib_formula_round(n):
    return int(((1 + math.sqrt(5)) / 2) ** n / math.sqrt(5) + 0.5)

#fib = lambda n:pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)
    
def fib_matrix(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
    
#print([fib_iterative(i) for i in range(90)])
#print([fib(i) for i in range(90)])
print(fib_iterative(10000))
#print(fib(20000))
      
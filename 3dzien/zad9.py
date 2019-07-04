# ciag fibonacciego - definiowanie fukcji
def  fib(n):
    i = 2
    x_prev = 1
    x_prevprev = 0
    while i <= n:
        xi = x_prev + x_prevprev # x(n) = x(n-1) + x(n-2)
        i += 1
        x_prev, x_prevprev = xi, x_prev
        # x_prevprev = x_prev
        # x_prev = xi
    return xi





def fib2(n):
    xn = [0, 1]
    i = 2
    while i <= n:
        xn.append(xn[i - 1]) + xn[i - 2]
        i += 1

    return xn[-1]


print(fib(7))
print(fib2(7))
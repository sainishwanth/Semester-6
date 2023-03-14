import sympy as sp

x = sp.Symbol('x')
f = 'x**3 - 4*x**2 + 2'
f_prime = str(sp.diff(f, x))
f = f.replace('**', '^')
f_prime = f_prime.replace('**', '^')

print(f'The derivative of {f} is {f_prime}.')
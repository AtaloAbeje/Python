# lambda = is a way to define a function that gets params and return 1 value
x1 = lambda y:y*2

print(x1(3))  # --> 6


sub = lambda z,w:z-w
div = lambda z,w:z/w
mul = lambda z,w:z*w
mod = lambda z,w:z%w

print(sub(9,4))  # --> 5
print(div(9,4))  # --> 2.25
print(mul(9,4))  # --> 36
print(mod(9,4))  # --> 1
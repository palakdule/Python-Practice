#recursion example
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(6)


#factorial example
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))


#Factorial
# n = 0
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

# f = factorial_iter(5)
f = factorial_recursive(4)
print(f)

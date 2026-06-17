#function definaton
def calc_sum(a, b): #parameters
    return a + b

sum = calc_sum(1,2) #function call; arguments
print(sum)


#example
def print_hello():
    print("hello")
print_hello()


#example
def print_hello():
    print("hello")

output = print_hello()
print(output) #none output


#avg of 3 number
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

calc_avg(98, 97, 95)

#product
def cal_prod(a=2 , b=4):
    print(a * b)
    return a * b

cal_prod()

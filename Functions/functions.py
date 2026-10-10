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


# marks1 = [45, 78, 86, 77]
# percentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400)*100

# marks2 = [75, 98,88,78]
# percentage2 = (sum(marks2)/400)*100
# print(percentage1, percentage2)


#function
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98,88,78]
percentage2 = percent(marks2)
print(percentage1, percentage2)


#Function with argument
def greet(name):
    print("Good Day, "+ name)

def mySum(num1, num2):
    return num1 + num2

greet("Palak")
s = mySum(6, 32)
print(s)


#default parameter value
def greet(name = "Stranger"):
    print("Good Day, "+ name)

greet("Palak")
greet()

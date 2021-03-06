# -*- coding: utf-8 -*-
##### Basic Functions I #####

# For each of the following code snippets, first predict the output
# (what you will see printed to the terminal). 
# Once you've made a prediction, run the code snippet to see if you are correct!


# 1
def a1():
    return 5
print(a1())

# Answer: 5
# Actual Output: 5 (TRUE)

# 2
def a2():
    return 5
print(a2()+a2())

# Answer: 10 # It will call a2() twice and sum the returned values 5+5 = 10
# Actual Output: 10 (TRUE)

# 3
def a3():
    return 5
    return 10
print(a3())

# Answer: 5 ## It will return the first return statement (return 5) and ignore the second because its unreachable code
# Actual Output: 5 (TRUE)

# 4
def a4():
    return 5
    print(10)
print(a4())

# Answer: 5 ## It will just return the return statement and ignore the print because its unreachable code
# Actual Output: 5 (TRUE)

#5
def a5():
    print(5)
x = a5()
print(x)

# Answer: Nothing ## Since the a5() is a void function it will return nonthing 
# Actual Output: it will print 5 when calling a5() but also X= None (Half-TRUE)

#6
def a6(b,c):
    print(b+c)
print(a6(1,2) + a6(2,3))

# Answer: 3, 5 # it will print the sum of 1 and 2 = 3 then the sum of 2 and 3 = 5 but 
# Nothing for the the third sum since the printed values are not numbers 

# Actual Output: It will print 3 and 5 then throw an error since the two operands are NoneType 
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType' (TRUE)

#7
def a7(b,c):
    return str(b)+str(c)
print(a7(2,5))

# Answer: 25 # it will return 25, the concatenation of the two args
# Actual Output: 25 (TRUE)

# 8

def a8():
 b = 100
 print(b)
 if b < 10:
    return 5
 else:
    return 10
 return 7

print(a8())

# Answer: 100 # it will print only the b value because it wrong putting several returns value in if statement
# Suggestion: its better to remove the else and the last return statement since it is unreachable

def a8_mine():
 b = 100
 print(b)
 if b < 10:
    return 5
 return 10

print(a8_mine())

# Actual Output: It will retrun nothing since the a8() has a syntax error *invalid character in identifier*  (Half - TRUE)

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# Answer: 7, 14, 21 # it will return 7 for the first call and 14 for the second since 5<3 then 21 for the third call 
# Suggestion: Removing the last return statement since its unreachable statement
# Actual Output: 7, 14, 21 (TRUE)

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# Answer: 8
# Suggestion: Removing the last return statement since its unreachable statement
# Actual Output: 8 (TRUE)

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# Answer: 500,  500, 300, 500 # it will assign 500 to b and print it, then it will print b again 500
# Next, calling a11() to print 300 then print the b again 500
# Actual Output: 500, 500, 300, 500 (TRUE)

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# Answer: 500,  500, 300, 500 # it will assign 500 to b and print it, then it will print b again 500
# Next, calling a12() to print 300 then print the b again 500
# Actual Output: 500, 500, 300, 500 (TRUE)

#13
b = 500
print(b)
def a13():
    b = 300
    print(b)
    return b
print(b)
b=a13()
print(b)

# Answer: 500,  500, 300, 300 # it will assign 500 to b and print it, then it will print b again 500
# Next, calling a13() to print 300 and assign the return value to the b then print new value of b which is 300
# Actual Output: 500, 500, 300, 300 (TRUE)

#14
def a14():
    print(1)
    b14()
    print(2)
def b14():
    print(3)
a14()
# Answer: 1, 3, 2 # it will print 1 then calling b to print 3 then retrun to print 2
# Actual Output: 1, 3, 2 (TRUE)

#15
def a15():
    print(1)
    x = b15()
    print(x)
    return 10
def b15():
    print(3)
    return 5
y = a15()
print(y)
# Answer: 1, 3, 5, 10
# when we call a15() will print 1 then calling b to print 3 and return 5 to the x variable then print x 
# next return 10 to the y and printing y 
# Actual Output: 1, 3, 5, 10 (TRUE)

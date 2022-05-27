# if 10 >5:
#     print("10 greater than 5")
    
#     num = 12
#     if num > 5:
#         print("bigger than 5")
#         if num <= 47:
#             print("between 5 and 47")
#     bigger than 5
#     between 5 and 47

#     x = 4
#     if x == 5:
#         print("yes")
#     else:
#         print("no")
#     no

#     num = 3 
#     if num == 1:
#         print("one")
#     else:
#         if num == 2:
#             print("two")
#         else:
#             if num == 3:
#                 print("three")
#     three

# num = 3
# if num == 1:
#     print("one")
# elif num == 2:
#     print("two")
# elif num== 3: 
#     print("three")
# else:
#     print("something else")

# print(1==1 and 2==2)
# print(1==1 and 2==3)
# print(1==2 or 3==2)
# print(1==1 or 2==3)
# print(not 2==2)
# print(not 2==3)
# print(False == False or True)
# print(False == (False or True))
# grade = 88
# if(grade>=70 and grade < 100):
#     print("passed")

# words = ["hello","world","again"]
# print(words)
# print(words[2])

# empty_list = []
# print(empty_list)

# num = 3
# n_list = ["string",0,[1,2,num],4.56]
# print(n_list[1])
# print(n_list[2])
# print(n_list[2][2])

# nestedl = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ,[10,11,12]
#     ]
# print(nestedl[0][1])
# print(nestedl[2][2])
# print(nestedl[0][0])
# print(nestedl[1][2])
# print(nestedl[3][2])
# print(nestedl[3][1])
# print(nestedl[3][0])
# print(nestedl[1][2])

# stng = 'hello world!'
# print(stng[11])
# print(stng[5])

# nums = [1,1,1,1,1,1]
# nums[2] = 6
# nums[4] = 'whaa'
# print(nums)

# nums = [1,2,3]
# numss = nums + [4,5,6]
# nums2 = [5,4,3,2,1,0]
# print(numss)
# print(nums2 + numss)
# print(nums*3)

# if 3 in nums2:
#     print(nums2[1])
    
# print(not 4 in nums)
# print(4 not in nums)

# nums.append(4)
# print(nums)
# print(len(numss))
# nums.insert(1, 'inserted')
# print(nums)

 # letters = [['p','q','r','s','t'],
 #           [8,7,6,5,4],
 #            ['a',2,'c',4,'e']]
# print(letters.index('c'))
# print(letters.index(5))

# print(nums.index('inserted'))
# max(numss)
# min(nums2)
# nums.count(4)
# nums2.remove(0)
# print(nums2)
# numss.reverse()
# print(numss)

# i=1
# while i<5:
#     print(i)
#     i = i + 1
# print('finished!')

# x=1
# while x<10:
#     if x%2 == 0:
#         print(str(x) + " is even")
#         x+=1
#     else:
#         print(str(x) + " is odd")
#         x+=1

# i=0
# while True:
#     print(i)
#     i+=1
#     if i>5:
#         print('breaking')
#         break
#     print('finished')

# i=0
# while i<5:
#     i+=1
#     if i==3:
#         print('skipping 3')
#         continue
#     print(i)
    
# words = ['x','y','z','a','b','c']
# for word in words:
#     print(word + "!")

# strng = 'testing for letters'
# count = 0

# for x in strng:
#     if (x=='t'):
#         count += 1
    
#     print(count)

# num = list(range(10))
# print(num)

# numbers = list(range(4,12))
# print(numbers)

# print(range(20) == range(0,20))

# num = list(range(5,20,2))
# print(num)

# num = list(range(20,5,-2))
# print(num)

# for i in range(5):
#     print('hello')

# fizzbuzz problem
# FizzBuzz is a well known programming assignment, asked during interviews.

# The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
# It takes an input n and outputs the numbers from 1 to n.
# For each multiple of 3, print "Solo" instead of the number.
# For each multiple of 5, prints "Learn" instead of the number.
# For numbers which are multiples of both 3 and 5, output "SoloLearn".

# You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.
# n = int(input())

# for x in range(1, n):
#     if x%2 == 0:
#         continue
#     if x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#     elif x % 3 == 0:
#         print("Solo")
#     elif x % 5 == 0:
#         print("Learn")
#     else:
#         print(x)

# def my_func():
#     print("do som")
#     print("i said do som")

# my_func()

# def P_W_E(word):
#     print(word + '!')
    
# P_W_E('spam')
# P_W_E(' eggs')
# P_W_E('python')

# def sumng(x,y):
#     print(x + y)
    
# sumng(5,4)

# def func(variable):
#     variable+=1
#     print(variable)

# func(7)

# def max(x,y):
#     if x >=y:
#         return x
#     else:
#         return y

# print(max(4,7))
# z= max(8 ,5)
# print(z)

# def multply(x,y):
#     return x*y

# a=4
# b=3

# op= multply
# print(op(a,b))

# def add(x,y):
#     return x+y

# def do_twice(func,x,y):
#     return func(func(x,y), func(x,y))
# a=5
# b=10

# print(do_twice(add, a, b))

# import random
# for i in range(5):
#     value =random.randint(1,6)
#     print(value)

# from math import pi,sqrt
# print(pi)
# print(sqrt(4))

# from math import sqrt as Square_Root
# print(Square_Root(100))

# You are making a Celsius to Fahrenheit converter.
# Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

# Sample Input
# 36

# Sample Output
# 96.8
# The following equation is used to calculate the Fahrenheit value: 9/5 * celsius + 32
# celsius = int(input())

# def conv(c):
#     return (9/5 * c) + 32
# fahrenheit = conv(celsius)
# print(fahrenheit)





























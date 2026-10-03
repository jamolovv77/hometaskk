
# def show_arguments(num):
#     print(f"Arguments: {num.__name__}")
#     def multiply(a,b):
#         print(a * b)

#     return multiply

# @show_arguments
# def multiply(a, b):
#     print(a,b)


# multiply(4, 5)








# def frame(num):

#     print("===========")
#     def name(num):
#         print(num)

#         print("===========")
#     return(name) 
  
# @frame
# def num(num):
#     print(num)

# num("Python")  





# def double_result(num):
#     def twice(name):
#         print(name *2)
#     return twice


# @double_result
# def get_number(namber):
#     print(namber)
# get_number(10)







# def multiply(num):
#     name=lambda a,b :(a * b)
#     return name


# @multiply
# def num1(num, name1):
#     print(num, name1)


# print(num1(6,7))









# def count_calls(func):
#     cnt=0
#     def hello(num):
#         nonlocal cnt
#         cnt+=1
#         print(f"Call:{cnt}")
#         return(num)
#     return hello


# @count_calls
# def name(num):
#     print(num)

# print(name("Hello"))
# print(name("Hello"))
# print(name("Hello"))










# def string_only(func):
#     def value(num):
#         if type(num) == str:
#             print(num)
#         else:

#             print("A string is required")
#     return value
    

    
# @string_only
# def string(num):
#     print(num)
    
# string(100)





# def adult_only(func):
#     def inner(age):
#         if age>=18:
#             print("Welcome")

#         else:
#             print("Access denied")

#     return inner

# @adult_only
# def enter_club(age):
#     print(age)


# enter_club(16)
# enter_club(20)





# students = [('Ali', 75), ('Sara', 92), ('Bob', 84)]
# sorted_students = sorted(students, key = lambda lam:lam[1], reverse = True)
# print(sorted_students)





# def add_prefix(func):
#     def inner(num):
#         print(f"Result: {num}")
#     return inner

# @add_prefix
# def get_name(name):
#     print(name)

# get_name("Ali")




# def check_division(func):
#     def inner(num1, num2):
#         if num2==0:
#             print("Cannot divide by zero")
#         else:
#             print(num1 / num2)
#     return inner



# @check_division
# def division(num1, num2):
#     print(num1, num2)
    
# division(10,0)






# num=list(map(int, input().split()))

# name=list(filter(lambda num: num> 0, num))

# print(name)



# first Question 

# def my_max(a,b,c):
#     if a>b and a>c:
#         print(a,"max")
#     elif b>a and b>c:
#         print(b,"max")
#     elif a==b:
#         print(a,"max")
#     else:
#         print(c,"max")

# n1=int(input("check your number:>"))
# n2=int(input("check your number:>"))
# n3=int(input("check your number:>"))

# my_max(n1,n2,n3)

# second Question

# def sum_list(n):
#     s=0
#     for i in n:
#         s=s+i
#     print(s)

# v=[1,2,3,4,5,6,7,8,9]
# sum_list(v)

# Third Question

# def sum_list(n):
#     s=1
#     for i in n:
#         s=i*s
#     print(s)

# v=[1,2,3,4,5,6,7,8,9]
# sum_list(v)

# four Question

# def reverse_string(a):
#     v=""
#     for j in a:
#         v=j+v
#     print(v)

# v="vishal"
# reverse_string(v)
# 
# Fifth Question

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input())
# print(factorial(n))

# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f

# v=int(input())
# print(factorial(v))
        
# sixth Question

# def check(x):
#     if x in range(50):
#         return True
#     else:
#         return False

# x = int(input("Enter a number: "))
# print(check(x))

# Seventh Question

# def upper_lower_c(n):
#     u=0
#     l=0
#     c=0
#     s=0
#     for i in n:
#         if i in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#             u+=1
#         elif i in ("1234567890"):
#             c+=1
#         elif i in ("!@#$%^&*()_+"):
#             s+=1
#         else:
#             l+=1
#     print("no. of upper:>",u,"no. of lower:>",l,"no. of digits:>",c,"no. of s:>",s)

# v=input()
# upper_lower_c(v)

# Eigth Question

# def unique(l):
#     n=[]
#     for i in l:
#         if i not in n:
#             n.append(i)
#     print(n)

# print(unique([1,2,3,3,3,3,4,5])) 

#################################################################################################################

# 15th Question

# n=int(input("enter your:>"))
# i=47
# if i in range(n):
#     print("yes")
# else:
#     print("yes")






# 16th Question

# def printValues(n):
# 	l = []
# 	for i in range(1,n+1):
# 		l.append(i**2)
# 	print(l)
		
# a=10
# printValues(a)

# 17th Question



# 19th Question

# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def greater_2(a,b,c):
#     if greater(a,b)>c:
#         return greater(a,b)
#     else:
#         return c
        
        
        
# v=int(input())
# v=int(input())
#  =int(input())
# print(greater(12,9))
# print(greater_2(12,4,9))


# a=int(input())
# b=0
# c=1
# i=0
# while i<=a:
#     print(b)
#     d=b+c
#     b=c
#     c=d
#     i+=1



############################################################
#prime number
# n=int(input("check your prime number\n"))
# for i in range(2,n):
#     if n%i==0:
#         print("No its not a prime")
#         break
# else:
#     print("Yes its Prime")
###############################
# nums=int(input())
# i=0
# sums=0
# count=0
# while (count<=nums):
#     if (i%2==0):
#         sums=sums+i
#         count=count+1
#     i=i+1
# print("v",sums,count,i,nums)

# i=int(input())
# sums=0
# while(i>0):
#     sums=sums+i%10
#     i=i//10
# print(sums)

# n=int(input())
# t=n
# r=0
# while (n>0):
#     d=n%10
#     r=r*10+d
#     n=n//10
# if(t==r):
#     print("P hai")
# else:
#     print("P nhi hai")    


#`frist_one`
# i=int(input())
# r=0
# while (i>0):
#     r=r+(i%10)*(i%10)
#     i=i//10
# print(r)

#second_one
# i=int(input())
# r=0
# while (i>0):
#     r=r+(i%10)*(i%10)*(i%10)
#     i=i//10
# print(r)

#third_one
# i=int(input())
# s=0
# while (i>0):
#     i=i//10
#     s+=1
# print("no. of digits",s)


# i=(input())
# v=""
# c=0
# while i in v:
#     i=i//str(10)
#     c=i+c
# print("no. of digits",i)

#forth_one
# i=int(input())
# r=i
# s=0
# while (i>0):
#     r=r+(i%10)*(i%10)*(i%10)
#     i=i//10
# if (r==s):
#     print("Armstrong hai")
# else:
#     print("Armstrong nhi hai")

# i=int(input())
# n=i
# s=0
# while (i>0):
#     i=i//10
#     s+=1
# print("no. of digits",s)
# s=0
# n=i
# while(i>0):
#     d=i%10
#     x=1
#     p=1
#     while (x<=s):
#         p=p*d
#         x+=1
#     s=s+p
#     i=i//10
# if (s==i):
#     print("Armstrong hai")
# else:
#     print("Armstrong nhi hai")

# i=int(input())
# s=0
# while (i>0):
#     i=i//10
#     s+=1
# print("no. of digits",s)
# # i=int(input())
# n=i
# s=0
# while (i>0):
#     n=n+(i%10)*(i%10)*(i%10)
#     i=i//10
# if (n==s):
#     print("Armstrong hai")
# else:
#     print("Armstrong nhi hai")

# i=int(input())
# pro=1
# while (i>0):
#     pro=pro*(i%10)
#     i=i//10
# print("no. of digits",pro)

# n=int(input())
# rec=0
# while (n>0):
#     rec=(rec*0)+i%10
#     n=n//10
# print(rec)

# a=["Vishal","suraj","23456"]
# b=[]
# for i in a:
#     v=""
#     for j in i:
#         v=j+v
#     b.append(v)
# print(b)

# a=list(input("enter your iteams:> "))
# b=[]
# for n in a:
#     v=""
#     for j in n:
#         v=j+v
#     b.append(v)
# print("this is your recverse list iteams:",b)




# list1=list(input())
# lit2=list(input())
# for i in lit2:
#     for j in list1:
#         if (i==j):
#             list1.remove(i)
# print(list1)


# i=0
# while(i<=100):
#     if i%7==0:
#         print(i)
#     i+=1


# i=0
# s=0
# while(i<=100):
#     s=s+i
#     i+=1
# print(s)


# i=int(input("how many times"))
# s=0
# v=1
# while(v<=i):
#     n=int(input("enter yo no."))
#     s=n+s
#     v+=1
# print(s)


# i=1
# while(i<=100):
#     if(i%2==0):
#         print(-i)
#     else:
#         print(i)
#     i+=1



# i = 556
# while i < 644:
#   z = i - 556
#   if z % 7 == 0:
#     print(z)
#   i = i + 1 

# x=int(input())
# c=0
# u=0
# # while x!=0:
# y=input()
# if y%2==0:
# 	c+=1
# else:
# 	u+=1
# x-=1
# if c>u:
# 	print("ready for watel")
# else:
# 	print("not")


# x=int(input())
# y=int(input())
# m=[]
# c=0
# n=0
# b=0
# while c!=x:
# 	m.append([])
# 	while n!=y:
# 		v=input()
# 		if v >="a" and v<="z" or v>="A" and v<="Z":
# 			m[b].append(v)
# 		elif v in "1234567890":
# 			v=int(v)
# 			m[b].append(v)
# 		else:
# 			v=float(v)
# 			m[b].append(v)
# 		n+=1
# 	n=0
# 	b+=1
# 	c+=1
# print(m)

# x=[1,2,3,[1,2,3],[1,1,"6"]]
# y=[]
# for i in x:
# 	if i in "1234567890":
# 		v=int(i)
# 		y.append(v)
# 	elif type(i)==[]:


# x=1
# y=2
# c=4
# while c!=0:
# 	if c%2==0:
# 		print(x,y,x,y)
# 	else:
# 		print(y,x,y,x)
# 	c-=1

# x=int(input())
# y=int(input())
# c=0
# while x!=0:
# 	x-=y
# 	c+=1
# print(c)

# x=int(input())
# y=int(input())
# m=[]
# c=0
# n=0
# b=0
# while c!=x:
# 	m.append([])
# 	while n!=y:
# 		v=input()
# 		if v in "1234567890":
# 			v=int(v)
# 			m[b].append(v)
# 		n+=1
# 	n=0
# 	b+=1
# 	c+=1
# print(m)

# =======================================================================================================
# frist Q1:>
# n=int(input())
# for i  in range(1,n+1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for v in range(0,i):
#         print("*",end="")
#     print()

#Second Q2:>
# n=input()
# m=""
# for i in n:
#     m=i+m
# if n==m:
#     print("Yes! this is Palindrome")
# else:
#     print("No! this is not Palindrome")

# Theird Q3:>
# n=int(input())
# for i in range(1,n+1):
#     for x in range(1,10+1):
#             print(i,"*",x,"=",i*x)
#    print()

# forth Q4:>

# n=int(input())
# f=1
# i=1
# while i<=n:
#     f=f*i
#     i+=1
# print(f)

# n=int(input())
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)

#fifth Q5:>


# n=int(input("print your fan seric:"))
# a = 0
# b = 1
# i = 0
# while i < n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     i+=1

# n=int(input("print your fabancci seric:"))
# a = 0
# b = 1
# for i in range(n):
#     print(a,end=",")
#     c=a+b
#     a=b
#     b=c
# print()

# n=int(input())
# c=0
# i=1
# while i<=n:
#     m=int(input())
#     c=m+c
#     i+=1
# print(c)


# list1=list(input())
# lit2=list(input())
# for i in lit2:
#     for j in list1:
#         if (i==j):
#             list1.remove(i)
# print(list1)




# def my_function(x):
#   return list(dict.fromkeys(x))

# mylist = my_function(["a", "b", "a", "c", "c"])

# def my_function(x):
#   return x[::-1]

# mytxt = my_function("I wonder how this text looks like backwards")

# print(mytxt)

# x=int(input("HOW MANY LIST YOU WANT:>"))
# m=[]
# b=0
# for i in x:
#     y=int(input("HOW MANY ITEAMS YOU WANT PUT:>"))
# 	m.append([])
# 	for i in y:
# 		v=input()
# 		if v in ("1234567890"):
# 			v=int(v)
# 			m[b].append(v)
#         elif if (v >="a" and v<="z") or (v>="A" and v<="Z"):
# 			m[b].append(v)
#         else:
# 			v=float(v)
# 			m[b].append(v)
# 	b+=1
# 	c+=1
# print(m)

# li=[i for i in range(100) if i%2==0]
# print(li)


# n=int(input())
# # s=0
# for s in range(1,n):
# # while s!=1 and s!=4:
#     # s=0
#     for s in range(n):
#     # while n>0:
#         t=n%10
#         s+=(t*t)
#         n=n//10
#     n=s
# if s==1:
#     print("happy")
# else:
#     print("not happy")


# n=int(input())
# i=2
# while n>=i:     
#     if n%i==0:
#         print("No P")
#         break
#     i+=1
# else:
#     print("YES P")

# n=int(input("check your number:> "))
# i=2
# while i<n:
#     if n%i==0:
#         print("Prime nhi hai ")
#         break
#     i+=1
# else:
#     print("Prime hai ")

# n=int(input("check your number:> "))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print("Prime hai")
# else:
#     print("Prime nhi hai")

# n=int(input("check your number:> "))
# c=0
# x=2
# while x<=n/2:
#     if n%x==0:
#         c=1
#         break
#     x+=1
# if c==0:
#     print("Prime hai")
# else:
#     print("Prime nhi hai")



#Fallten list
# l1=[[1,2,3,4,4,4,9],[9,8,6,],[4,2,6,8,5]]
# l2=[]
# for i in l1:
#     for j in i:
#         l2.append(j)
# print(l2)

# l1=[1,2,3,4,[1,2,3,4,4,4,9],1,2,3]
# l2=[]
# for i in l1:
#     l2.append(i)
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#         else:
#             l2.remove(i)
# print(l2)

#Extra Question

# ni=int(input("how many times you want to added:> "))
# new_list=[]
# i=0
# while i<ni:
#     n=int(input("number of times:> "))
#     new_list.append(n)
#     i+=1
# print(new_list)


#frist question

# a = [1,2,3,4,5,6,7,8]
# b = [a[-1]]+a[:-1]
# print("old list:",a)
# a = (b)
# print("new list:",a)

# second question
# v=int(input())
# i=0
# a=[]
# while i<v:
#     print("Enter number")
#     num = input()
#     a.append(num)
#     i = i+1
# n = input("check your number\n")
# if n in a:
#     print("Yes")
# else:
#     print("No")

# third question

#len function code:>

# v=["vishal",24,7,9,5]
# v="123456734567"
# c=0
# for i in v:
#     c+=1
# print(c)

# v1="123456734567"
# print(sum(1 for ch in v1))

 
# sm = [23, 45, 89, 90, 56, 80] 
# l = len(sm)
# i = 0
# tm = 0 
# # for i in sm:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# while i < len(sm):
#     tm = sm[i] + tm
#     i = i + 1
# print ("Total Marks: " + str(tm))



# name = ["Savitri", "Phule", "26"]
# print (name[0]+" "+name[1])


# name = ["Savitri", "Phule", "26"]
# c=0
# while c!=name:
#     c+=1
# print(c)


# n=int(input())
# n1=int(input())
# c=0
# co=0
# while c<n1:
#     co=co+n
#     c+=1
# print(co)



# v = [23, 45, 89, 29, 56, 80]
# for i in v:
#     if i>20 and i<40:
#         print(v.index(i))

# v=int(input())
# i=0
# a=0
# while i<50:
#     a,i=a,b
#     c=a+c
#     print(c)
#     i+=1 


# l1=[1,2,3,[4,6],[2,5]]
# newl=[]
# for i in l1:
#     newl.append(i)
#     if type(i)==list:
#         for j in i:
#             newl.append(j)
# print(newl)

# l1=[1,2,3,4,[1,2,3,4,4,4,9],1,2,3]
# l2=[]
# for i in l1:
#     l2.append(i)
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#             if type(i)==list:
#                 for j in i:
#                     l2.append(j)
#             else:
#                 l2.remove(i)
# print(l2)

# print("Welcome to the Indusind Bank")
# pin=int(input("enter your 4 digit pin"))
# if pin==2020:
#     print("1.withdraw")
#     print("2.balance enquiry")
#     print("3.deposit")
#     print("4.exit")
#     a=int(input())        
#     if a==1:
#         print("enter amount ")
#         amount=int(input())
#         print("transaction successful")
#         print("your remaining amount is", 1000-amount)
#     elif a==2:
#         print("1000")
#     elif a==3:
#         print("enter your deposit amount")
#         amount=int(input())
#         print("your currently amount is",1000+amount)
#     elif a==4:
#         print("thank you")
#     else:
#         print("cash is not in the ATM")
# else:
#     print("wrong pin")


# player1=input("")
# player2=input("")
# if player1=="stone" and player2=="paper":
#     print("player2 won the game")
# elif player1=="stone" and player2=="scissor":
#     print("player1 won the game")
# elif player1=="paper" and player2=="stone":
#     print("player1 won the game")
# elif player1=="paper" and player2=="scissor":
#     print("player2 won the game")
# elif player1=="scissor" and player2=="stone":
#     print("player2 won the game")
# elif player1=="scissor" and player2=="paper":
#     print("player1 won the game")
# else:
#     print("draw the game")


# a=20
# b=int(input("enter the number"))    
# if a==b:
#     print("you won the game")
# else:
#     print("try again")
#     c=int(input("enter the number"))
#     if a==c:
#         print("you won the game")
#     else:
#         print("try again")
#         d=int(input("enter the number"))
#         if a==d:
#             print("you won the game")
#         else:
#             print("you lost the game try to next time")



# a=20
# t=0
# for i in range(3):
#     b=int(input("enter the number"))
#     if a==b:
#         print("you won the game")
#         break
#     elif b<a:
#         print("try again")
#         t+=1
#     else:
#         print("try again")
#         t+=1
# if t>2:
#     print("you lose the game")


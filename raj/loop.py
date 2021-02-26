'''
a = 1
while a<100:
	print(a+1)
	a+=1	

x = 1
while x<15:
	print(x*7)
	x+=1


x = 0
y = 100
while y>=0:
	x+=y
	y-=1
pri
nt(x)


x=1 
while x<10:
	y = int(input("type an number:   "))
	y+=y
print(y)



y=1
while y<=100:
	if(y%2==1):
		print(y)
	else:
		print(y*-1)	
	y+=1

c=0
y=1
while y<=10:
	x = int(input("type an number:  "))
	z = x+c
	c+=x
	y+=1
print(z)	
w = 1
e = 2
c = 0
x = 5
while x>=0:
	print("w "*c,end="")
	print()
	c+=1
	x-=1

x=1
while x<=100:
	if (x%3==0):
		print("Nav")
		x+=1
	else:
		if (x%7==0):
			print("Gurukul")
			x+=1
		else:
			if (x%3==0) and (x%7==0):
				print("Navgurukul")
				x+=1
			else:
				print(x)
				x+=1


a = 156
y = a-155
while y<=10:
	print(y)
	y+=1

n = int(input("type an number:  "))
o=n
while o>=2:
	x=int(input("type an number: "))
	o-=1
	z = x+n
	n+=x
print(z)

x = int(input("type an number:  "))
y=1
while y<=1:
	if x==2 or x==3 or x==5 or x==7 or x==13:
		print("the number is prime: ")
		y+=1
	else:
		if x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%13==0 or x%11==0:
			print("the number is not prime:  ")
			y+=1
		else:
			print("the number is prime: ")
			y+=1

y=5
x=5
while y>=1:
	print(5*str(x),end="")
	print()
	x-=1
	y-=1

x=20
while x<=100:
	print(x)
	x+=2

x=7
while x<=100:
	print(x)
	x+=7

y=12
x=412
while x>=0:
	y+=x	
	x-=1
print(y)

x=30
y=420
while y>0:
	x+=y
	y-=8
print(x)

c=0
x=0
while x<=10:
	y = int(input("type the weight: "))
	z=y+c	
	c+=y
	x+=1
	e = c/11
if e%5==0:
	print(e,"the weight is divisival by 5")
else:
	print(e,"the weight is not divisival by 5")

x=1
while x<=100:
	print(x)
	x+=1
	print(-x)
	x+=1


e=0
while e<=5:
	y = int(input("type any number 1 to 10:    ")) 
	if y==5:
		print("your gess is wright")
		break

	else:
		if y<5:
			print("your gess is less the my number:  ")
		else:
			if y>5:
				print("your gess is greater than my number:  ")
			print("pleas try again")
		e+=1
if y!=5:
	print("you loos ")

c = 0
d = 1

while c < 3:
    c = c + 1
    d = d * c
    print "Loop Ke Andar", c, d
else:
    print "Loop Ke Bahar", c, d

n = 6
s = 0
i = 1

while i <= n:
    s = s + i
    i = i + 1

print s

i = 0
while(i<5):
    j = 0
    while(j<5): #loop2
        if (j > 3): 
            break 
        else:
            print "*", 
        j = j + 1    
    print ''
    i = i + 1


x = 0
while(x<7):
    if (x == 3 or x==5):
        x = x + 1
        continue
    print(x)
    x = x + 1

index = 1
while index < 10:
    print(index)
    index = index + 1

i=0
while i<10:
	j = 0
	while j<=5:
		print(j)
		j = j + 1
	i = i + 1

# i = 0
# num = int(input("Enter your number:- "))
s# while(i <= num):
# 	if(num > 0):
# 		print("it is positive")
# 	elif(num < 0):
# 			print("it is negetive")
# 	else :
# 		print("zero")	
# 	i = i + 1
# x = 365
# print(x*16+4)


# x=16*12
# z=1
# y=16
# print(x*30+y*5+z*y/4 , "days")

x=int(input("type number of students:  "))
y=int(input("type amount of one student"))
if x*y<50000:
	print("kaaracha baagaata kaa aanndar ha ")
else:
	print("kaaracha baajaaata kaa baahar ha ")

x = int( input("type an number:  "))
y=x-1
while y>0:
	x*=y
	y-=1
print(x)

x = int(input("type an number:   "))
while x>0:
	z=x
	c=1
	while z>0:
		print(" "*z,end="")
		print(" *"*c,end="")
		print()
		c+=1
		z-=1
		x-=1	

x = int(input(" type an number:  "))
i=1
while i<=x:
	j=1
	while j<=x:
		print(j,end=" ")
		j+=1
	i+=1
	print()

x = int(input("type an number:  "))
i=1 
while i==1:
	j=1
	while j<=1:
		print(j,end=" ")
		j+=1
		print()
	i+=1

	j=1
	while j<=1:
		print(j,end=" ")
		j+=1
		print()
	i+=1

x = int(input("type an number:  "))
i=1 
while i==1:
	print()


x = int(input("type an number:  "))
if x==1:
	print("it is co-prime")
else:
	if x==2 or x==3 or x==5 or x==7 or x==13:
		print("it is  prime")
	else:
		if x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%13==0: 
			print("it is not prime")
		else:
			print("it is prime ")




# x=int(input("type an year:  "))
# if x%4==0 and x%400==0 or x%100!=0:
# 	print("it is leapyear")
# else:
# 	print("it is not leapyear")





y="asdfghjklzxcvbnmqwertyuiop"
x=input("type your name:  ")
for a in y:
	z.append(a)
for j in x:
	if j in z:
		z.remove(j)
print(z)

# x=(input('type an number:   '))
# y=x[::-1]
# print(int(y))

# x=int(input("type an number:   "))
# y=x
# while x>0:

x=int(input("type an number:  ")) 
n=x 
y=0 
while x>0: 
	z=x%10 
	y=y*10+z
	x=x//10 
if(n==y):
	print("it is palandrom") 
else:
	print("it is not palandrom")


# x = int(input("type an number:  "))
# y = int(input("type an number:  "))
# z = int(input("type an number:  "))
# if x==y==z:
# 	print("type unequal number")
# 	if x>=y>=z:
# 		print(y)
# 	else:
# 		if z==y<x:
# 			if y>=x>=z:
# 				print(x)
# 			else:
# 				if y>=z>=x:
# 					print(z)
# 				else:
# 					if z>=y>=x:
# 						print(y)
# 					else:
# 						if z>=x>=y:
# 							print(x)
# 						else:
# 							if x==y<z:
# 								print(z)
# 							else:
								
# 									print(x)
# 								else:
# 									if z==x<y:
# 										print(y)
# 									else:
# 										print(z)	

x=int(input("type an number:  "))
y=int(input("type an number:  "))
z=int(input("type an number:  "))
if x+y>z:
	if x+z>y:
		if z+y>x:
			print("its make a triangle")
		else:
			print("its neaver make triangle")
	else:
		print("its neaver make triangle")
else:
	print("its naver make triangle")

# x=int(input("type an angle:  "))
# y=int(input("type an angle:  "))
# z=int(input("type an angle:  "))
# if x==0 or y==0 or z==0:
# 	print("these angle neaver make triangle")
# else:
# 	if x+y+z==180:
# 		if x==y==z:
# 			print("it is equlateral triangle")
# 		else:
# 			if x==y or y==z or x==z:
# 				print("it is isoselas triangle")
# 			else:
# 				if x==90 or y==90 or z==90:
# 					print("it is right angle triangle")
# 				else:
# 					if x!=y!=z:
# 						print("it is scaler triangle")
# 	else:
# 		print("the sum of angle is not 180")

# x=int(input("type the numbers of the years:   "))
# b=0.24*x/100
# if x%400!=0 and x%24!=0:
# 	while x!=(x%4==0):
# 		x+=1
# 		if x%400==0 or x%4==0:
# 			if x%100!=0:
# 				print(x)
# 				print(x+4)
# 				print(x+8)
# 				break
# else:
# 	print(x+4)
# 	print(x+8)
# 	print(x+12)

import time
v1 = time.time()
x=int(input("type an number:  "))
y=1
c = 1
while x>=1:
	y+=1
	if y==2 or y==3 or y==5 or y==7 or y==11 or y==13: 
		print(c," - ",y)
		c+=1
		x-=1
	else:
		if y%2!=0 and y%3!=0 and y%5!=0 and y%7!=0 and y%11!=0 and y%13!=0:
			print(c," - ",y)
			x-=1
			c+=1

# v2 = time.time()
# print("sec-  ",v2-v1)

import time
p1=time.time()
x = int(input("type an number:  "))
y=1
c=0
while y<=x/2:
	if x%y==0:	
		c=y+c
	y+=1	
if c!=x:
	print("it is not perefect number")
else:
	print("it is perefect  number")
p2=time.time()
print(p2-p1)

x = int(input("type an number:  "))
c=x-1
y=x*c
while c>=2:
	c-=1
	y=y*c
print(y)

x=int(input("type an number:  "))
n=x
c=0
b=0
while x!=0:
	y=x%10 
	x//=10
	c+=y
	if c!=1:
		while c>=2:
			c-=1
			y=c*y
		c=0
		b+=y
	else:
		b=b+1
if b==n:
	print("it is strong number")
else:
	print("it is not strong number")

x=int(input("type an number:  "))
n=x
c=0
while x!=0:
	y=x%10
	x//=10
	v=y**3
	c+=v
if c==n:
	print("it is armstrong number")
else:
	print("it is not armstrong number")



x=int(input("type an number:  "))
y=int(input("type an number:  "))
z=int(input("type an number:  "))
b=int(input("type an number:  "))
if x==y and z==b or z==x and y==b or x==b and y==z:
	print("these sides are of rectengle sides")
else:
	print("these sides are not of rectengle sides")

x="asfrt(1256734)sdfgh"
print(x[6:-6])


x=input("type an number: ")
b=len(x)
y=len(x)/2
if b%2==0:
	z=x[0:int(y)]
	c=x[int(y):b]
	o={}
	u={}
	for y in z:
		if y not in o:
			o[y]=1
		else:
			o[y]+=1
	for i in c:
		if i not in u:
			u[i]=1
		else:
			u[i]+=1	
	if o == u:
		print("it is leapendrom1")
	else:
		print("it is not leapendrome2")
else:
	z=x[0:int(y)]
	c=x[int(y+1):int(b)]
	for g in z:
		g in z
	if g in c:
		print("it is leapenderome")
	else:
		print("it is not leapendrome") 






y = int(input("type an number:  "))
x=1
v=1
while v<=y:
	x+=1
	if x==2 or x==3 or x==5 or x==7 or x==13 or x==11:
		print(x)
		v+=1
	else:
		if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%13!=0 and x%11!=0:
			print(x)
			v+=1
	

# import time
# p1=time.time()
# for x in range(1,int(input("type an number:  ")),+1):
# 	y=1
# 	c=0
# 	while y<=x:
# 		y+=1
# 		if x%y==0:
# 			c=y+c  
# 			if c==x and x!=1:
# 				print(x,"is prime number")
# 				p2=time.time()
# 				print(p2-p1)import time
# p1=time.time()
# for x in range(1,int(input("type an number:  ")),+1):
# 	y=1
# 	c=0
# 	while y<=x:
# 		y+=1
# 		if x%y==0:
# 			c=y+c  
# 			if c==x and x!=1:
# 				print(x,"is prime number")
# 				p2=time.time()
# 				print(p2-p1)
	# else:
# 	print("start:---",x)
# 	print("it is not ")
# 	p2=time.time()
# 	print(p2-p1)



# x=int(input("type an number:  "))
# y=0
# c=0
# while y!=x:
# 	y+=1
# 	while x%y==0:    
       

# import time
# p1=time.time()
# x = int(input("type an number:  "))
# y=1
# c=0
# while y<=x/2:
# 	if x%y==0:	
# 		c=y+c
# 	y+=1	
# if c!=x:
# 	print("it is not perefect number")
# else:
# 	print("it is perefect  number")
# p2=time.time()
# print(p2-p1)



# import time
# p1=time.time()
# for x in range(1,int(input("type an number:  ")),+1):
# # x=int(input())
# 	y=1
# 	c=0
# 	print("x",x)
# 	while y<=x:
# 		y+=1
# 		if x%y==0:
# 			c=y+c 
# 			print("y",y)
# 			print("c",c)  
# 			if c==x and x!=1:
# 				print("start:--",x)
# 				print("it is perefect number")
# 				p2=time.time()
# 				print(p2-p1)import time
# import time
# p1=time.time()
# for x in range(1,int(input("type an number:  ")),+1):
# # x=int(input())
# 	y=0
# 	c=0
# 	while y<=x:
# 		y+=1
# 		if x%y==0:
# 			c=y+c   
# 			if c==x and x!=1:
# 				print("start:--",x-(x-1))
# 				print(x,"is perefect number")
# 				p2=time.time()
# 				print(p2-p1)

x = "ghjdophdj(ghjdhsjkh)ghdshdj"


# x="ghjdophdghjdhsjjkh(Himachal)ghdshdj"
# y = x.index("(")
# z = x.index(")")
# print(x[y+1:z])
# x="ghjdophdghjdhsjjkh(Himachal)ghdshdj"
# # z=[]
# # for i in x:
# # 	z.append(i)
# # 	if i!="(":
# # 		z.remove(i)
# # 		for  i in z:
# # 			if i!=")":
# # 				print(i,end="")
# # print(x)
# for i in range(len(x)):
# 	if x[i]!="(":
# 		y = x[i+2:]
# 	else:
# 		x[i]=="("
# 		break
# for j in y:
# 	if j!=")":
# 		print(j,end="")
# 	else:
# 		j==")"
# 		break
# print()
# print(new)




# for y in x:
# 	if "(" in y:	
# 		for z in x:


# x="ghjdophdghjdhsjjkh(Himachal)ghdshdj"

# for i in range(len(x)):
# 	if x[i]=="(":
# 		y=i+1
# 	if x[i]==")":
# 		z=i
# print(x[y:z])

x=[1,2,3,4]
y=[1,2,3,4]
z=0
while z<=3:
	print(x[z]*y[-z-1])
	z+=1

x=input("type any thing:  ")
z=[]
b=[]
c="!"
for y in x:
	l=0
	for g in x:
		if y==g:
			l+=1	
	print(y,l)


x=input("type your name:  ")
b={}
for y in x:
	if y not in b:
		b[y]=1
	else:
		b[y]+=1
print(b)

# x = [0,2]

# print(x)

# x[0] = 1

# print(x)

# x[1] = 3

# print(x)



# x=input("type any thing:  ")
# print(type (x))
# y=["q","w","e","r","t","y"]
# print(z)




y=[[1,2,3],[1,2,3],[1,2,3]]
h=0
for x in y:
	for c in x:
		h+=c
print(h)

x = [1,2,[ 1 , 5 , 3 ], [ 2 , 7 , 8 ], [ 4 , 6 , 9 ],5]
h=len(x)
k=0
g=0
while k!=h:
	d=x[k]
	k+=1
	g+=d
print(g)

# x=input("type an number: ")
# b=len(x)
# y=len(x)/2
# if b%2==0:
# 	z=x[0:int(y)]
# 	c=x[int(y):b]
# 	for g in z:
# 		g in z
# 	if g in c:
# 		print("it is leapendrom1")
# 	else:
# 		print("it is not leapendrome2")
# else:
# 	z=x[0:int(y)]
# 	c=x[int(y+1):int(b)]
# 	for g in z:
# 		g in z
# 	if g in c:
# 		print("it it s leapenderome")
# 	else:
# 		print("it is not leapendrome") 



import random
x=["vishal panda","rohit","modi","saabed","rajeshwer","anand","omash","sonu","vishal majundar","akhilesh","yusuf","bijander","atul","tarique","akash","bashkar","shubham","rahul","deepak serma","rakesh","ramesh","chandan","sankara vivak","thaman","kalil","deepak patal","kartik","prakash","yoogaas","aajeet","sadik","ranjan","praabaker","santos","reeyaz","alok","roshan"]																															
room1=["sonu","yoogaas","ranjan"]
room6=["saabed","thaman","vishal majundar","prakash","ramesh","modi"]
room7=["aajeet","omash","bijander","akhilesh","kalil","siddik"]
room8=["vishal panda","rajeshwer","shubham","deepak serma","kartik,akash"]
room10=["sankara vivak","atul","chandan","yusuf","tarique"]
room11=["deepak patal","rahul","rakesh","bashkar"]
g=[[],[],[],[],[],[],[]]
no=36
bad=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","10","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52"]
b=0
k=0
n=0
f=0
d=0
o=0
r=0
z=[]
while b!=36:
	p=random.randint(0,35)
	if p not in z:
		if p in room1 and k!=8:
			m=random.randint(1,6)
			ccc=g[m]
			ccc.append(x[p])
			print(ccc,"1")
			b+=1
			k+=1
			z.append(p)
			continue
		elif p in room6 and n!=10:
			m=random.randint(0,5)
			cc=g[m]
			cc.append(x[p])
			print(cc,"2")
			z.append(p)
			n+=1
			b+=1
			continue
		elif p in room7 and f!=8:
			m=random.randint(0,5)
			oo=g[m]
			oo.append(x[p])
			print(oo,"3")
			z.append(p)
			f+=1
			b+=1
			continue
		elif p in room8 and d!=6:
			m=random.randint(0,5)
			c=g[m]
			c.append(x[p])
			print(c,"4")
			d+=1
			z.append(p)
			b+=1
			continue
		elif p in room10 and o!=8:
			m=random.randint(0,5)
			q=g[m]
			q.append(x[p])
			print(q,"5")
			z.append(p)
			o+=1
			b+=1
			print("yuu")
			continue
		elif p not in room1 and room6 and room7 and room8 and room10 and r==10:
			m=random.randint(0,5)
			u=g[m]
			u.append(x[p])
			print(u,"6")
			z.append(p)
			r+=1
			b+=1
			print("ak")
			continue
		else:
			continue
	else:
		continue
print(b)
'''

# y=int(input("type an number:  "))
# c=0
# while y>=1:
# 	y=y//10 
# 	c+=1
# print(c)


# for i in range(10,1,-1):
	# print(i)


# x="abcd"
# y=len(x)
# n=""
# while y!=0:
# 	y-=1
# 	z=x[y]
# 	n+=z
# print(n)


# x=input("type any thing:  ")
# z=[]
# c=""
# for i in x:
# 	if i==" ":
# 		z.append(c)
# 		c=""
# 	else:
# 		c+=i
# z.append(c)
# print(z)



# def ok(n):
# 	while n<=100:
# 		if n%2==0:
# 			print("even",n)
# 			n+=1
# 		else:
# 			if n%2!=0 and n:
# 				return n+ok(n)
# 				n+=1
# print ('odd',ok(1))

# x=[1,2,3,5,1]
# v=0
# m=[]
# while m!=x:
# 	c=x[v]
# 	m.append(c)
# 	v+=1
# print(v)	



# x=[12,123,23,24,25,34,36,37,73,4]
# v=0
# n=0
# m=0
# while v!=len(x):
# 	c=x[v]
# 	m=x[v+1]
# 	if n<c:
# 		print(c)
# 		if n>m:
# 			n=m
# 			print(n)
# 	v+=1
# print(n)

# import time
# p1=time.time()
# m=0
# x=1
# b=0
# y=int(input("type an number:  "))
# print(m)
# print(x)
# while b<y:
# 	n=x+m
# 	print(n)
# 	m=x
# 	x=n
# 	b+=1
# p2=time.time()
# p=(p2-p1)
# print(p)
	







# def ok(n):
#     while n<=100:
#         if n%2!=0 and n==100:
#             return 1    
#         else:
#             print("even",n)
#             n+=2
#             return (n+ok(n))
#             print(n)

                
# print ('odd',ok(2))



# x=int(input("type an number:  "))
# y=int(input("type an number:  "))
# b=int(input("type an number:  "))
# while b!=0:
# 	print(x)
# 	x+=y
# 	print(y)
# 	y+=x
# 	b-=1




# x=1
# b=0
# c=101
# while b!=200:
# 	if x>=101:
# 		if x%2!=0:
# 			x+=1
# 			m=x-c
# 			print(m)
# 		else:
# 			x+=1
# 	else:
# 		if x%2==0:
# 			print(x)
# 			x+=1
# 		else:
# 			x+=1
# 	b+=1

# counter = 0
# count = 2
# count_ = 1
# while counter<100 :
# 	if counter<50 :
# 		print(count)
# 		count+=2
# 	else:
# 		print(count_)
# 		count_+=2
# 	counter+=1	



# x =["1.haaamara daas ka praadan mantery kon ha","2.duuneya kaa sabaasa gaahara saamudraa koon sa ha","3.duneya kaa saabaasa uucha praabaatha koon sa ha"]
# c=["1. jaabaahar laal naaharu", "2.  narander daamodar daas mode", "3. funsuuk baagdu" ,"4. kamalas ","1.  hind maaha saagar" ,"2. praasan maaha saagaar" ,"3. baagaal kee kaade" ,"4. atlantic osion","1.  Kaalaas paarabat","2. mount evarest","3. k2","4. araabale"]
# z=0
# v=0
# y=0
# while y<=3:
# 	while z<=3:
# 		print(x[z])
# 		print(c[v])
# 		z+=1
# 		v+=1
# 	y=int(input("chouse your option:  "))
# 	if y==2 or y==4 or y==6:
# 		print("your anser is wright\nyou win 4 cror rupes")
# 		print("your next qustion is")
# 		y+=1
# 	else:
# 		print("your anser is wrong")
	
# print("thankyou")

# x=[1,3,2,4,2,5,4,6,4,6]
# k=[]
# p=0
# n=0
# b=0
# while p!=len(x):
# 	o=x[p]
# 	p+=1
# 	for i in x:
# 		n+=1
# 		print(o)
# 		print(n)
# 		print(len(x),b)
# 		if b<=o and n==len(x):
# 			print("r")
# 			k.append(b)
# 			k.append(l)
# 			print(k)
# 			n=0
# 		else:
# 			if i<o:
# 				b=i
# 			else:
# 				if i==o:
# 					l=i
# 					x.remove(i)

# print(k)


# import Time

# y = [64, 34, 25, 12, 22,12, 11, 90]  
# n = 0
# while n!=len(y):  
# 	for i in range(0, len(y)-n-1): 
# 		if y[i] > y[i+1] : 
# 			y[i+1],y[i] = y[i],y[i+1] 
# 	n+=1
# print(y)



# import random 

# def win():
#     print ('You win!')


# def lose():
#     print ('You lose!')

# while True:
# 	player = input('What do  you pick? (rock, paper, scissors)')
# 	# player_choice.strip( )
# 	random_move = random.randint(0, 2)
# 	moves = ['rock', 'paper', 'scissors']
# 	computer = moves[random_move]
# 	if player == computer:
# 		print ('Draw!')
# 	elif player == 'rock' and computer == 'scissors':
# 		win()
# 	elif  player == 'paper' and computer == 'scissors':
# 		lose()
# 	elif player == 'scissors' and computer == 'paper':
# 		win()
# 	elif player == 'scissors' and computer == 'rock':
# 		lose()
# 	elif player == 'paper' and computer == 'rock':	
# 		win()
# 	elif player == 'rock'  and computer == 'paper' :
# 		lose()
# 	again = input('Do you want to play again?: y and for stop n)')
# 	if again == 'n':
# 		break





# bb=""
# b=0
# chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# x=int(input("if you want incresable password then type 1 or if you want dreaciable passward then type 2:  "))
# if x==1:
# 	x=input("type your passward:  ")
# 	for y in x:
# 		for c in chars:
# 			if b!=25 and b!=24 and c==y:
# 				b+=2
# 				bb+=chars[b]
# 				b=0
# 				break
# 			else:
# 				if b==25 and c==y:
# 					bb+=chars[1]
# 					b=0
# 					break
# 				if b==24 and c==y:
# 					bb+=chars[0]
# 					b=0
# 					break
# 			b+=1
# 	print(bb)
# else:
# 	if  x==2:
# 		x=input("type your passward:	")
# 		for y in x:
# 			for c in chars:
# 				if c==y and b!=0 and b!=1:
# 					b-=2
# 					bb+=chars[b]
# 					b=0
# 					break
# 				else:
# 					if c==y and b==0:
# 						bb+=chars[24]
# 						b=0
# 						break
# 					if c==y and b==1:
# 						bb+=chars[25]
# 						b=0
# 						break
# 				b+=1
# 	print(bb)




# x=0
# g=0
# while x!=len(a):
# 	v=a[x]
# 	x+=1
# 	g+=v
# print(g)


# def z(y):
# 	c=0
# 	if type(y)==list:
# 		for i in y:						
# 			if type(y)==list:
# 				z(i)
# 			else:
# 				c+=y
# 				print(c,"r")
# 	else:
# 		c+=y
# 		print(c,"o")
# 	print(c)
# y=[0,[1,2,3],[3,[4],5],[[5,6]]]
# print(z(y))



# y=int(input("type any number to factorial:	"))
# x=y-1
# while x!=0:
# 	y*=x
# 	x-=1
# print(y)



# def find_in_list(query, mainlist):
#     mainlist_len = len(query)
#     range_for_loop = range(mainlist_len)
#     index = 0
#     for i in range_for_loop:
#         element = mainlist[i]
#         print(query)
#         print(element)
#         if element == query:
#             index = i
#     return i
# print(find_in_list(["a"],["s","d","f","g","h","j"]))



# x = open("r.py")
# y= x.read()
# print (y)
# x.close()


# x = open("r.py","a")
# x.write("Abhishek - Gurgaon")
# x.close()
# x=open("r.py")
# y=x.read()
# print(y)
# x.close()




# m = open("r.py", "w")
# m.write("Abhishek - Gurgaon\n")
# m.write("Ranveer - Delhi")
# m.close()
# x=open("r.py")
# y=x.read()
# print(y)
# x.close()






# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("<html>\n")
# students_file.write("<head>\n")
# students_file.write("<title>NavGurukul Students</title>\n")
# students_file.write("</head>\n")
# students_file.write("<body>\n")
# students_file.write("<ul>")
# for student in batch1_students:
#     students_file.write("<li>" + student + "</li>\n")
# students_file.write("</ul>\n")
# students_file.write("</body>\n")
# students_file.write("</html>\n")
# students_file.close()



	# 	if c%2==0:
	# 		print(x,y,x,y)
# x=open("r.py")
# y=x.read()
# print(len(y))


# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# x=open("r.py","w")import json
# y=open("r.text")
# z=y.readlines()
# c={}
# f=""
# for i in z:
# 	x=i.split(" ")
# 	h=x[1:]
# 	for i in h:
# 		i+=" "
# 		print(i)
# 	c[x[0]]=i
# 	print(c)
# print(c)
# b=open("r.json","a")
# json.dump(c,b,indent=4)
# y.close()

# for y in banks_list:
# 	x.write(y+"\n")
# x.close()





# f=open("r.txt")
# v=f.readlines()
# x=1
# for i in v:
# 	if "\n" in i:
# 		x+=1
# print(x)




# v=input("type your name:	")
# x=input("type your state:	")
# v=[v,x]
# if "delhi" in v[1]:
# 	with open("index.py","a") as g:
# 		g.write(v[0]+"\n")
# 		# g.close()
# elif "shimla" in v[1]:
# 	c=open("r.py","a")
# 	c.write(v[0]+"-"+"shimla"+"\n")
# 	c.close()
# else:
# 	x=open("ranjan.py","a")
# 	x.write(v[0]+"\n")
# 	x.close()

# x=int(input())
# if x%3==0 and x%5==0:
# 	print("fizz,buzz")
# elif x%3==0 and x%7==0:
# 	print("fizz,bizz")
# elif x%5==0 and x%7==0:mport time
# p1=time.time()
# m=0
# x=1
# b=0
# y=int(input("type an number:  "))
# print(m)
# print(x)
# while b<y:
# 	n=x+m
# 	print(n)
# 	m=x
# 	x=n
# 	b+=1
# p2=time.time()
# p=(p2-p1)
# print(p)
# 	print("buzz,bizz")
# elif x%3==0:
# 	print("fizz")
# elif x%5==0:
# 	print("buzz")
# elif x%7==0:
# 	print("bizz")
#else:
#	print("nothing")


# x=int(input())
# y=int(input())
# c=0
# while x!=0:
# 	x-=y
# 	c+=1
# print(c)


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

# def x(y, j):
#     v = len(y)
#     b = range(v)
#     l = 0
#     for i in b:
#         k = j[i]
#         print(y)
#         print(k)
#         if k == y:
#             l = i
#     return i
# print(x(["a"],["s","d","a","g","h","j"]))


# def z(y):
# 	c=0
# 	if type(y)==list:
# 		for i in y:						
# 			if type(y)==list:
# 				z(i)
# 			else:
# 				c+=i
# 	else:
# 		print(c)
# y=[0,[1,2,3],[3,[4],5],[[5,6]]]
# print(z(y))

# y=[0,[1,2,3],[3,[4],5],[[5,6]]]
# c=[]
# if type(y)==[]:
# 	for i in y:
# else:
# 	c.append()




# import json

# k ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }


# x=open("r.json","w")
# json.dump(k,x,indent=21)
# x.close(	)	

# import json
# x={"fghj":8}
# y=json.dumps(x)
# print(y)



# import json
# x={"Name":"Ram", 
#   "Class":"IV", 
#   "Age":9 }
# h=open("if.py","a")
# y=json.dump(x)
# h.write(y)
# h.close()



# import json
# x={
# 	"name": "David",
# 	"class":"I",
# 	"age": 6  
#   }
# h=open("r.json","a")
# j=json.dump(x,h,indent=4)
# h.close()



# import json
# x={}
# h=open("r.json","a")
# json.dump(x,h,indent=4)
# h.close()

# import json
# x= {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# y=open("r.json","a")
# json.dump(x,y,indent=4)
# y.close()

# x={
#  "a": 1,
#  "a": 2,
#  "a": 3, 
#  "a": 4,   
#  "b": 1, 
#  "b": 2
#  }
# y={}
# y["a"]=x["a"]
# y["b"]=x["b"]
# print(y)


# import json
# y=open("r.text")
# z=y.readlines()
# c={}
# f=""
# for i in z:
# 	x=i.split(" ")
# 	h=x[1:]
# 	for i in h:
# 		f=f+i+" "
# 	c[x[0]]=f
# 	f=""
# b=open("r.json","a")
# json.dump(c,b,indent=4)
# y.close()





# import json
# x=[["neelam","programer","24","2400"],
#    ["komal","trainer","24","20000"],
#    ["anuradha","HR","25","4000"],
#    ["Abhishek","manager","29","63000"]]
# y=["name","designation","age","salary"]
# z=["emp1","emp2","emp3","emp4"]
# c={}
# g=0
# a={}
# v=0
# for i in x:
# 	while g!=len(x):
# 		c[y[g]]=i[g]
# 		g+=1
# 	a[z[v]]=c
# 	v+=1
# 	g=0
# 	c={}
# x=open("r.json","a")
# json.dump(a,x,indent=4)
# x.close()


# import json
# x={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
# y=open("n.json","w")
# json.dump(x,y,indent=2)
# y=open("n.json")
# m=json.load(y)
# l=input("type what you want:	")
# y=int(input("type number of items:	"))
# f=int(x["shopping_list"][l])-y
# x["shopping_list"][l]=str(f)
# y=open("n.json","w")
# json.dump(x,y,indent=2)

# import json
# def signup(e,p):
# 	x=open("n.json")		
# 	y=json.load(x)
# 	m={}
# 	m["email"]=e
# 	m["passward"]=p
# 	m["todo"]={"0":"aganda"}
# 	y.append(m)
# 	a=open("n.json","w")
# 	json.dump(y,a,indent=4)
# 	print("signup is sucesfull")
# def login(e,p,):
# 	x=open("n.json")
# 	y=json.load(x)
# 	f=[]
# 	for i in y:
# 		for u in i:
# 			f.append(u)
# 	for o in f: 	
# 		if i[o]==e and i[o]==p:
# 			print("susfull login")
# 			q=input("you want to read your ageanda or wright (r or w):	")
# 			if "r" in q:
# 				print(i["todo"])
# 				break 
# 			else:
# 				print(i["todo"])
# 				z=input("type your aggeda:	")
# 				h=i["todo"]
# 				for c in h:
# 					c=c
# 				u=int(c)
# 				pp=i["todo"]
# 				pp[str(u+1)]=z
# 				q=open("n.json","w")
# 				json.dump(y,q,indent=4)
# 				break
# 		else:
# 			print("your email id is wrong")
# x=input("what you want (login,signup):	")
# if "l" in x:
# 	x=input("type your email id")
# 	y=input("type your email id passward")
# 	login(x,y)
# else:
# 	x=input("type your email id")
# 	y=input("type your email id passward")
# 	signup(x,y)




# y = [1]  
# n = 0
# u=len(y)
# while n!=u:  
# 	for i in range(0, len(y)-n-1): 
# 		if y[i] > y[i+1]: 
# 			y[i+1],y[i] = y[i],y[i+1] 
# 	n+=1
# n=0
# d=[]
# print(y)
# for i in y:
# 	if i in d:
# 		y.remove(i)
# 	else:
# 		d.append(i)
# if len(d)>=2:
# 	print(d[-2])
# else:
# 	print("there is no 2")

# Question=1

# a="ranjan"
# b=0
# for i in a:
# 	b=b+1
# print(b)

# a=int(input('enter : '))
# for i in range(a):
# 	print("* "*(a))
# print()

# n=int(input("enter a number:"))
# x=0
# y=1
# z=0
# while z<=n:
# 	x=y
# 	z=x
# 	z=x+y
# 	print(z)


# a="sdfghjsdfgh"
# for i in a:
# 	print(i)

# for x in range(2, 10):
#     if(x==7):
#         break
#     print(x)


# for x in range(2, 10):
#     if(x==7):
#         continue
#     print(x)



# import time
# import multiprocessing
# import json
# import requests
# from bs4 import BeautifulSoup as b
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys 
# PATH="/home/navgurukul/Downloads/chromedriver"
# time.sleep(2)
# driver=webdriver.Chrome(PATH)
# driver.get("https://www.flipkart.com/home-entertainment/pr?sid=ckf&otracker=categorytree")
# time.sleep(2)
# link=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')   
# link.send_keys("tv")
# link.send_keys(Keys.RETURN)
# time.sleep(2)
# filter=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/section[4]/div[2]/div[1]/div[1]/input')
# filter.send_keys("sony")
# filter.send_keys(Keys.RETURN)
# time.sleep(2)
# click=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div/section[4]/div[2]/div[1]/div[2]/div/div/label/div[2]')
# click.click()
# time.sleep(1)
# filter=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[2]/input')
# filter.send_keys("LG")
# filter.send_keys(Keys.RETURN)
# xz=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[3]/div/div')
# xz.click()
# fg=driver.current_url
# r=requests.get(str(fg)).text
# rr=b(r,"html.parser")
# tyu=rr.find("div",class_="_3LxdjL _3NzWOH")
# x=tyu.find("div",class_="E2-pcE _3zjXRo")
# p=x.find_all("div",class_="_2pi5LC col-12-12")
# p.pop(-1)
# lkj=p.pop(-1)
# pol=[]
# mnb=lkj.find("nav",class_="yFHi8N")
# mnb=mnb.find_all("a",class_="ge-49M")
# for i in mnb:
#         i=i.get("href")
#         pol.append(i)
# def cod(url):
#         dic={}
#         lis=[]
#         qu=[]
#         r=requests.get("https://www.flipkart.com/"+str(url[0])).text
#         rr=b(r,"html.parser")
#         print(rr)
#         tt=rr.find("div",class_="_3LxdjL _3NzWOH")
#         tyur=tt.find("div",class_="_3FqKqJ")
#         rrr=tyur.find("div",class_="E2-pcE _3zjXRo")
#         p=rrr.find_all("div",class_="_2pi5LC col-12-12")
#         p.pop(0)
#         p.pop(0)
#         for i in p:
#                 a=i.find("div",class_="_2kHMtA")
#                 link=a.find("a")["href"]
#                 aaa=a.find("div",class_="_3pLy-c row")
#                 d=aaa.find("div",class_="col col-7-12")
#                 a=d.find("div",class_="_4rR01T").get_text()
#                 dic["model"]=a
#                 q=d.find("div",class_="gUuXy-")
#                 if q==None:
#                         dic["reating"]="no reating"
#                 else:
#                         q=q.find("div",class_="_3LWZlK").get_text()
#                         dic["reating"]=q
#                     w=d.find("div",class_="fMghEO")
#                     w=w.find_all("li",class_="rgWa7D")
#                     for i in w:
#                             aa=i.get_text()
#                             qu.append(aa)
#                     dic["qualites"]=aa
#                     z=aaa.find("div",class_="col col-5-12 nlI3QM")
#                     z=z.find("div",class_="_30jeq3 _1_WHN1").get_text()
#                     z.replace("\u20b9"," ")
#                     dic["amount"]=z
#                     rr=requests.get("https://www.flipkart.com"+str(link)).text
#                     bs=b(rr,"html.parser")
#                     xz=bs.find("div",class_="_1YokD2 _3Mn1Gg")
#                     cv=xz.find("div",class_="K4SXrT funtru")
#                     if cv==None:
#                             pou=xz.find("div",class_="_16PBlm")
#                             iop=pou.find("div",class_="t-ZTKy")
#                             kjh=iop.find("div").div.get_text()
#                             dic["diccription"]=kjh
#                     else:
#                             vb=cv.find("div",class_="_3qWObK").get_text()
#                             hj=cv.find("div",class_="_3zQntF").p.get_text()
#                             dic["discription"]=[vb,hj]
#                     dic['link']=link
#                     gh=open("n.json","w")
#                     lis.append(dic)
#                     json.dump(lis,gh,indent=4)
#                     dic={}
#                     qu=[]
#         time.sleep(1)
# yui=[]
# for url in pol:
#         t1=multiprocessing.Process(target=cod,args=[url])
#         t1.start()
#         time.sleep(1)
#         yui.append(t1)
# for threds in yui:
#         threds.join()

# import json
# o=open("r.json")
# d=json.load(o)
# dic={}
# print(len(d))
# for i in d: 
# 	for ii in i:
# 		k=i[ii]
# 		l=k['direacter']
# 		if l not in dic:
# 			dic[l]=1
# 		else:
# 			s=dic[l]
# 			s+=1
# 			dic[l]=s
# oo=open("n.json","w")
# json.dump(dic,oo,indent=4)



# lk=0
# dic={}
# for i in l:
# 	for ii in i: 
#         k=i[ii]
#         l=k["language"]
#         dic[l]=lk+=1



# import time
# p1=time.time()
# s=""
# y=[]
# lo=0
# for i in s:
# 	l=s[lo:]
# 	k=i
# 	for ii in l:
# 		if ii not in k:
# 			k+=ii
# 		else:
# 			y.append(len(k))
# 			k=""
# 			k+=ii
# 	y.append(len(k))
# 	lo+=1
# if len(y)!=0:
# 	print(max(y))
# print(len(y))
# p2=time.time()
# print(p2-p1)


x=int(input())
yy=1
while True:
	x=str(x)
	y=x[::-1]
	y=int(y)
	x=int(x)
	x+=y
	x=str(x)
	if x==x[::-1]:
		print(int(x))
		break
	yy+=1

		
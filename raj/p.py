# import random
# print("welcome to hangman")
# t=open("r.text")
# r=t.readlines()
# w=random.randint(0,1)
# w=r[w]
# l=0
# wo=""
# z=""
# while l!=10 or w != wo :
# 	x=input("guss your letter:	")
# 	if x in w:
# 		print("your gess is wright")
# 		c=0
# 		for i in w:
# 			b=" "
# 			if i==x:
# 				p=(z+i)
# 				wo+=p
# 				print(wo)
# 			else:
# 				c+=1
# 				z=b*c
# 	else:
# 		print("good luck for next time")
# 		l+=1





# 

# def x(h):
# 	if h in [1,0]:
# 		return 1
# 	else:
# 		return x(h-1)+x(h-2)
# print(x(int(input())))

# s,j=[],int(input())
# for i in range(1,(j//2)+1):
# 	s.extend([i,13*i,7+(i-1)])
# print(s[j-1])

# x,c=list(map(int,input().split())),0
# for i in x:
# 	x.pop(0)
# 	if i in x:
# 		c+=1
# print(c)

# y,x=int(input()),int(input())
# for i in range(1,(min(x,y)+1)):
# 	if x%i==0 and y%i==0:
# 		d=i
# print((x*y)//d,"LCM","\n",d,"HCF")



# x=[15,7,11,2]
# y=11
# b=0
# for i in range(len(x)):			
# 	if b==1:
# 		break
# 	else:
# 		for u in range(len(x)):
# 			if i==u:
# 				continue
# 			if y==x[i]+x[u]:
# 				print(i,u)
# 				b=1



# a=input()
# a=list(a)
# count=0
# l=0
# while a:
# 	a.remove(a[l])
# 	count+=1
# print(count)

# ,"span",class_="secondaryInfo","span",class_="secondaryInfo","td",class_="ratingColumn imdbRating","strong",title="9.2 based on 2,320,529 user ratings"
# title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman"

# import requests
# from bs4 import BeautifulSoup
# x="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# v=requests.get(x).text
# with open("r.text","w") as h:
# 	h.write(v)
# 	h.close()
# s=BeautifulSoup(v,"html.parser")
# f=s.find('tbody',class_="lister-list").find_all('tr')
# # q=f.find_all('tr')
# print(f)


# x=input()
# x=list(x)
# res=[]
# i=['1','2','3','4','5','6','7','8','9','0']
# ii=i
# f=['1','2','3','4','5','6','7','8','9','0','.']
# c=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']
# for p in x:
# 	if p in i:
# 		i.remove(p)
# 		continue
# print(i)
# if i in ii:
# 	print("int")
# if res in s:
# 	print("string")
# if res in f:
# 	print("float")
# while (i>0):
#     n=n+(i%10)*(i%10)*(i%10)
#     i=i//10
# if res in c:
# 	print("complex")
 	
# 	if x in "1234567890.":
# 		r+=1
# if len(i)==q:
# 	print("int")
# else:
# 	print(q)
# if len(x)==w:
# 	print('string')
# if len(x)==r:
# 	print("float")
# print(len([1,2,3])/2)

# y=[]
# z=0
# s=input()
# s=list(s)
# xx=-1
# for i in s:
#     x=s.pop()
#     if x in s:
#         for i in s:
#             print(i)
#             if i==x:
#                 y.insert(z,i)
#                 s.remove(i)
#                 y.insert(xx,i)
#                 z+=1
#                 xx-=1
# yu=""
# for i in y:
#     yu+=i
# print(yu)

# a=[]
# X=input()
# x=list(X)
# d=0
# if len(x)>2:
#     for i in X:
#         p=x.pop(0)
#         if i in x:
#             a.append(i)
#             for u in x:
#                 print(a,u)
#                 if i==u:
#                     a.append(i)
#                     u=a
#                     a.reverse()
#                     print(a)
#                     if a==u:

#                         d=1
#                         print("".join(a))
#                         break
#                     else:
#                         break
#                 else:
#                     a.append(u)
#             if d==1:
#                 break
# else:
#     if len(x)==2:
#         if x[0]==x[1]:
#             print("".join(x))
#         else:
#             print(x[0])
#     else:
#         print(x[0])        

# a=[1,2,3,4,5,6,7,8,9]
# aa=[]
# for i in a:
#     b=max(a)
#     c=min(a)
#     aa.append(b)
#     aa.append(c)
#     a.remove(b)
#     a.remove(c)
# print(aa)
#                   
# h="hgfg"
# t=list("hf")
# x=list("hgfg")
# for i in t:
# 	for u in x:
# 		if u !=i:
# 			print(h.replace(i,"_"))
	# print(k)
	# break		
	print(h)

'''

x = input("type an passward of 8 digest to 16 digest:  ")
y = ["!","@","#","$","%","^","^","&"]
z = ["A","S","D","F","G","H","J","K","L","M","N","B","V","C","X","Z","Q","W","E","R","T","Y","U","I","O","P"]
d = ["a","s","d","f","g","h","j","k","l","m","n","b","v","c","x","z","q","w","e","r","t","y","u","i","o","p"]
c = ["1","2","3","4","5","6","7","8","9","0"]
h = len(x)
if (x in y) and (x in z) and (x in d) and (x in c) and (h<=16) and (h>=8):
	print("strong passward")
else:
	print("weak passward")





time = input("Is it morning or evening? (morning/evening) ")
if time == "morning":
    print ("Let's go for a run!")
elif time == "evening":
    print ("Let's go out for a coffee.")
elif time == "night":
	print("lets go for sleep")
else:
    print ("Mujhe samajh nahi paata")









food = input("aaj kaana ma kyaa bnaana ha (bhandi/gobhi)")
if food == "bhandi":
	print("bhandi kaaraab ho gahi ha ees leya aaj bhandi nahi baana gee")
elif food == "gobhi":
	print ("theek ha bhandi baanaa daatha ha ")
else:
	print("gobhi kaalo cuup chaap ")







if feal == "fine":
	print("oor baataaoo nooe taage") 
elif feal == "not good":
	print("kyaa hoo gaayaa")
else:
	print("kyaa baataa raahaa ho muuja saamj ne aayaa")




a=int(input("put your number"))
b=int(input("put your number"))
rr = a//b
print(rr)
if a>b:
	print(True)
elif a==b:
	print("equal")
else:
	print(False)







a = int(input("enter your value"))
b = int(input("enter your value"))
x = int(input("enter paasword: "))
if x==4510:
	print("\t\twelcome")
	p1 = input("player1 chose (stone/paper/seaser):  ")
	p2 = input("player2 chose (stone/paper/seaser):  ")
	if p1=="paper" and p2=="paper":
		print("draw")
	elif p1=="stone" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="seaser":
		print("player 1 wins ")
	elif p1=="paper" and p2=="stone":
		print("Player 1 wins ")
	elif p1=="paper" and p2=="seaser":
		print("Player 2 wins ")	
	elif p1=="seaser" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="seaser" and p2=="stone":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="stone":
		print("draw")
	elif p1=="seaser" and p2=="seaser":
		print("draw")
	else:
		print("baavkuuf kaalnaa nee aata")
else:
	print("wrong paasword (try agan)")






import random
ran = random.randint(0,2)
lis = ["stone","paper","seaser"]
p2 = lis[ran]

x = int(input("enter paasword: "))
if x==4510:
	print("\t\twelcome")
	p1 = input("player1 chose (stone/paper/seaser):  ")
	p2 = input("player2 chose (stone/paper/seaser):  ")
	if p1=="paper" and p2=="paper":
		print("draw")
	elif p1=="stone" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="seaser":
		print("player 1 wins ")
	elif p1=="paper" and p2=="stone":
		print("Player 1 wins ")
	elif p1=="paper" and p2=="seaser":
		print("Player 2 wins ")	
	elif p1=="seaser" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="seaser" and p2=="stone":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="stone":
		print("draw")
	elif p1=="seaser" and p2=="seaser":
		print("draw")
	else:
		print("baavkuuf kaalnaa nee aata")
else:
	print("wrong paasword (try agan)")






import random
lock = int(input("enter paas word: "))
if lock==4510:
	print("\t\twelcome to the game\n\t\twhen you leave the game\tpress  (0)")
	c2 = 5
	while c2==5:
		p3 = random.randint(0,2)
		lis = ["stone","paper","seaser"]
		computer = lis[p3]
		player = input("chose (stone/paper/seaser): ")
		if (computer=="stone" and player=="stone" or computer=="paper" and player=="paper" or computer=="seaser" and player=="seaser"):
			print("computer choose ",computer)
			print("****draw****")
		elif computer=="stone" and player=="paper":
			print("**computer choose**",computer)
			print("****you win****")
		elif computer=="stone" and player=="seaser":
			print("**computer choose** ",computer)
			print("****you lose****")
		elif computer=="paper" and player=="stone":
			print("**computer choose**",computer)
			print("****you lose****")
		elif computer=="paper" and player=="seaser":
			print("**computer choose**",computer)
			print("****you win****")
		elif computer=="seaser" and player=="stone":
			print("**computer choose**",computer)
			print("****you win****")
		elif computer=="seaser" and player=="paper":
			print("**computer choose**",computer)
			print("****you lose****")
		elif player=="0":
			break
		else:
			print("baavakuuf kaalaana nee aata")
else:
	print("kon haa baa tu ")




print("when you back to the informer******type v")
z = 3
while z==3:
	x = int(input("******type any number:  "))
	x%2
	if x%2==0:
		print("even")
	elif x%2!=0:
		print("odd")
	else:
		print("type any inteser")



x = int(input("type an any inteser:  "))
if x%2==0 and x>200:
	print("Bingo")
elif x%2!=0 and x<200:
	print("Ringo")
else:
	print("python")



x = int(input("type an inteser:  "))
y = int(input("type an another inteser:"))
if x>y:
	print(x)
elif x<y:
	print(y)


x = int(input("type the length of  1side : "))
y = int(input("type the length of another side:  "))
if x==y:
	print("these are of squre sides ")
else:
	print("these are of rectangle sides")





time = input("Is it morning or evening? (morning/evening) ")
if time == "morning":
    print ("Let's go for a run!")
elif time == "evening":
    print ("Let's go out for a coffee.")
elif time == "night":
	print("lets go for sleep")
else:
    print ("Mujhe samajh nahi paata")









food = input("aaj kaana ma kyaa bnaana ha (bhandi/gobhi)")
if food == "bhandi":
	print("bhandi kaaraab ho gahi ha ees leya aaj bhandi nahi baana gee")
elif food == "gobhi":
	print ("theek ha bhandi baanaa daatha ha ")
else:
	print("gobhi kaalo cuup chaap ")








a = 10
if a * 2 == 20:
print ("a variable ko 2 se multiply kar ke 20 aata hai")
else:
print ("Nah! a variable ko 2 se multiply kar ke 20 nahi aata.")













if feal == "fine":
	print("oor baataaoo nooe taage") 
elif feal == "not good":
	print("kyaa hoo gaayaa")
else:
	print("kyaa baataa raahaa ho muuja saamj ne aayaa")





a=int(input("put your number"))
b=int(input("put your number"))
rr = a//b
print(rr)
if a>b:
	print(True)
elif a==b:
	print("equal")
else:
	print(False)






x = int(input("enter paasword: "))
if x==4510:
	print("\t\twelcome")
	p1 = input("player1 chose (stone/paper/seaser):  ")
	p2 = input("player2 chose (stone/paper/seaser):  ")
	if p1=="paper" and p2=="paper":
		print("draw")
	elif p1=="stone" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="seaser":
		print("player 1 wins ")
	elif p1=="paper" and p2=="stone":
		print("Player 1 wins ")
	elif p1=="paper" and p2=="seaser":
		print("Player 2 wins ")	
	elif p1=="seaser" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="seaser" and p2=="stone":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="stone":
		print("draw")
	elif p1=="seaser" and p2=="seaser":
		print("draw")
	else:
		print("baavkuuf kaalnaa nee aata")
else:
	print("wrong paasword (try agan)")

  


import random
ran = random.randint(0,2)
lis = ["stone","paper","seaser"]
p2 = lis[ran]

x = int(input("enter paasword: "))
if x==4510:
	print("\t\twelcome")
	p1 = input("player1 chose (stone/paper/seaser):  ")
	p2 = input("player2 chose (stone/paper/seaser):  ")
	if p1=="paper" and p2=="paper":
		print("draw")
	elif p1=="stone" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="seaser":
		print("player 1 wins ")
	elif p1=="paper" and p2=="stone":
		print("Player 1 wins ")
	elif p1=="paper" and p2=="seaser":
		print("Player 2 wins ")	
	elif p1=="seaser" and p2=="paper":
		print("Player 2 wins ")
	elif p1=="seaser" and p2=="stone":
		print("Player 2 wins ")
	elif p1=="stone" and p2=="stone":
		print("draw")
	elif p1=="seaser" and p2=="seaser":
		print("draw")
	else:
		print("baavkuuf kaalnaa nee aata")
else:
	print("wrong paasword (try agan)")






import random
lock = int(input("enter paas word: "))
if lock==4510:
	print("\t\twelcome to the game\n\t\twhen you leave the game\tpress  (0)")
	c2 = 5
	while c2==5:
		p3 = random.rand(0,2)
		lis = ["stone","paper","seaser"]
		computer = lis[p3]
		player = input("chose (stone/paper/seaser): ")
		if (computer=="stone" and player=="stone" or computer=="paper" and player=="paper" or computer=="seaser" and player=="seaser"):
			print("computer choose ",computer)
			print("****draw****")
		elif computer=="stone" and player=="paper":
			print("**computer choose**",computer)
			print("****you win****")
		elif computer=="stone" and player=="seaser":
			print("**computer choose** ",computer)
			print("****you lose****")
		elif computer=="paper" and player=="stone":
			print("**computer choose**",computer)
			print("****you lose****")
		elif computer=="paper" and player=="seaser":
			print("**computer choose**",computer)
			print("****you win****")
		elif computer=="seaser" and player=="stone":
			print("**computer choose**",computer)
			print("****you win****")
		elif computer=="seaser" and player=="paper":
			print("**computer choose**",computer)
			print("****you lose****")
		elif player=="0":
			break
		else:
			print("baavakuuf kaalaana nee aata")
else:
	print("kon haa baa tu ")





while z==3:
	x = int(input("******type any number:  "))
	x%2
	if x%2==0:
		print("even")
	elif x%2!=0:
		print("odd")
	else:
		print("type any inteser")




x = int(input("type an any inteser:  "))
if x%2==0 and x>200:
	print("Bingo")
elif x%2!=0 and x<200:
	print("Ringo")
else:
	print("python")




x = int(input("type an inteser:  "))
y = int(input("type an another inteser:"))
if x>y:
	print(x)
elif x<y:
	print(y)




x = int(input("type the length of  1side : "))
y = int(input("type the length of another side:  "))
if x==y:
	print("these are of squre sides ")
else:
	print("these are of rectangle sides")




x = int(input("put any inteaser  number:  "))
y = int(input("put an another inteaser number:  "))
z = input("what you want (addasion(+)/substraction(-)/multiplay(*)/divide(/))\n****(+)****(-)*****(*)*****(/)")
if z=="+":
	print(x+y)
elif z=="-":
	print(x-y)
elif z=="*":
	print(x*y)
else:
	print(x/y)





num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")





								
x = input("type an passward of 8 digest to 16 digest:  ")
h = len(x)
if h<=16 and h>=8:
	if "0" in x or "1" in x or "2" in x or "3" in x or "4" in "5" or "6" in x or "7" in x or "8" in x or "9" in x:
		if "a" in x or "s" in x or "d" in x or "f" in x or "g" in x or "h" in x or "j" in x or "k" in x or "l" in x or "m" in x or "n" in x or "b" in x or "v" in x or "c" in x or "x" in x or "z" in x or "q" in x or "w" in x or "e" in x or "r" in x or "t" in x or "y" in x or "u" in x or "i" in x or "o" in x or "p" in x:
			if "!" in x or "@" in x or "#" in x or "$" in x or "%" in x or "^" in x or "&" in x:
				if "A" in x or "S" in x or "D" in x or "F" in x or "G" in x or "H" in x or "J" in x or "K" in x or "L" in x or "M" in x or "N" in x or "B" in x or "V" in x or "C" in x or "X" in x or "Z" in x or "Q" in x or "W" in x or "E" in x or "R" in x or "T" in x or "Y" in x or "U" in x or "I" in x or "O" in x or "P" in x:
					print("strong passward")

				else:
					print("your passward does not have any captial alfaabat")
			else:
				print("your passward does not have any spacel creacter")
		else:
			print("your passward does not have any small alfaabat")
	else:
		print("your passward does not have any digit")
else:
	print("the length of you passward is leas then or greater then 8 or 16:\n pleace try an another passward ")








x = int(input("taype any number:  "))
if x>200:
	if x%2==0:
		print("bingo")
	else:
		print("python")
else:
	if x<200:
		if x%2==1:
			print("ringo")
		else:
			print("pthon")





x = input("chose language (English_=1 or Hindi=2):   ")
if x=="1" or x!="1":
	y = int(input("pleace enter pin code:  "))
	if y==1234:
		f = input("type 6 for withdraw or type 7 for taking information):  ")
		a = "6"
		s = "7"
		if f==a:
			c = input("type 2 for saving account or type 3 for crant account):  ")
			e = "2"
			h = "3"
			if c==e:
				print("you can withdraw maximum (30,000rupees):\n\tof 500 nots:   ")
				z = int(input("Enter your amount----:   ")) 
				if z%500==0:
					print("thankyou")
			else:
				print("you can withdraw maximum (50,000rupees):\n\tof 500 nots:   ")
				c = int(input("Enter your amount-----:  "))
				if c%500==0:
					print("thankyou")
				else:
					print("the ATM has only of 500 nots ")
		else:
			if f==s:
				n = input("type 6 for taking information of saving account \ntype 7 for taking information of crant account:  )")
				f = "6"
				if n==f:
					print("you account have range of (30,000)rupees")
					u = input("for mor information type @: ")
					q = "@"
					if u==q:
						print("your account have range of (30,000)rupees.\nAnd your account have 15,000.")
					else:
						cc = "@"
						while cc=="@":
							print("for more information type @: ")
							d = input("-----")
							if d=="@":
								print("your account have range of (30,000)rupees.\nAnd your account have 15,000.")
								break
				else:
					print("your account have range of (50,000) rupees")
					d = input("for more information type @:  ")
					o = "@"
					if d==o:
						print("your account have range of (50,000).\nAnd your account have 30,000 rupees.")
					else:
						aa = "@"
						while aa=="@":
							print("for more information type @: ")
							d = input("------")
							if d=="@":
								print("your account have range of (50,000).\nAnd your account have 30,000 rupees.")
								break
			else:
				print("type 6 for taking information of saving account \ntype 7 for taking information of crant account: ")				


	else: 
		print("your pin code is wrong\n pleace try agan: ")
	





x = int(input("1 type any number------:   "))
y = int(input("2 type an another number-----:   "))
z = int(input("3 type an another number-----: "))
if x>y>z:
	print("number 1 is the greater one1")
else:
	if y>x>z:
		print("number 2 is the greater one2 ")
	else:
		if z>y>x:
			print("number 3 is the greater one3 ")
		else:
			if x>z>y:
				print("number 1 is the greater one4")
			else:
				if y>z>x:
					print("nuumber 2 is the greater one5 ")
				else:
					if z>x>y:
						print("number 3 is the greater one6 ")
					else:
						if x>y==z:
							print("number 1 is greater one ")
						else:
							if y>x==z:
								print("number 2 is greater one ")
							else:
								if z>y==x:
									print("number 3 is greater one ")
								else:
									if x<y==z:
										print("number 1 is luus and number 2 and 3 are equal")
									else:
										if y<x==z:
											print("number 2 is luus and 1 and 3 are equal")
										else:
											if z<x==h:
												print("number 3 is luus and 1 and 2 are equal")
											else:
												if x==y==z:
													print("all the numbers are equal")








x = int(input("type a number which  you want table:    "))
y = x*1
a = x*2
s = x*3
d = x*4
f = x*5
g = x*6
h = x*7
j = x*8
k = x*9
l = x*10
if x:
	print(x,"* 1  =",y)
	print(x,"* 2  =",a)
	print(x,"* 3  =",s)
	print(x,"* 4  =",d)
	print(x,"* 5  =",f)
	print(x,"* 6  =",g)
	print(x,"* 7  =",h)
	print(x,"* 8  =",j)
	print(x,"* 9  =",k)
	print(x,"* 10 =",l)


x = int(input("type an input where you want the sum of numbers:   "))
y = (1+x)/2
if x:
	print(y*x)




x = int(input("type the number which you want the table "))
a=1
while a<=10:
	print(x,"*",a,"=",a*x)
	a=a+1


	
c = 1
while c<=10:
	print(2,"*",c,"=",c*2)
	c+=1




x = 0
y = 10
while y>=0:
	x+=y
	y-=1
print(x)




x = int (input("type an number: "))
for y in range(x):
	for z in range(1,y+1):
		print(y,end="")
	print()





s = 0 
for y in range(1,21):
	if y>=0:
		s+=y
		y-=2
print(s)





a = 2
while a<=10:
	y = (a%2==0)
	print(a)
	a+=2


x = int("1")
for z in range(x):
	print(x,end=" ")
print()




n = 10
y = n 
for b in range(n+1,0): 
    	print(" ",end="")  
print(" ")
for x in range(0,n+1):
	print("* ",end="")
	



b=0
n = int(input("type an number:   "))
while n >=0:
	print(n*" " ,end="")
	print(b*"*")
	b+=1
	n-=1
print(" ")





a = 22
y=a/2
while y<=20:
	print(int(y-10))
	y+=1




a = 22
while a>=12:
	 print(int(a-a+1))
	y-=1 




# x=1
# y=1
# z=0
# while y<=2:
# 	print(x+z)
# 	print()
# 	print(x,z+2)
# 	print()
# 	x=11**2
# 	y+=1




x = int( input("type an number:  "))
for row in range(x,0,-1):
	for col in range(1,row+1):
		print(col,end="")
	print()




x = 1
y=int(input("typr an number:  "))
c = y-1
for z in range(0,2*c+1):
	if z<c:
		print("*"*x)
		x+=1
	else:
		print(("*"*x))
		x-=1




x=0
def ask_question():
	print("Mark Zuckerberg")
	print("Bill Gates")
	print("Steve Jobs")
	print("Larry Page")
while x<=100:
	print("Who is the founder of Facebook?")
	ask_question()
	x+=1
'''



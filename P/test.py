# a=[[1,2,3,34,3],["vishal"]]
# a[1].reverse()

# list1=[1,2,3,4,5,6,7,8]
# list2=[1,2,3,4]
# for i in list2:
#     for j in list1:
#         if (i==j):
#             list1.remove(i)
# print(list1)

# n=list(int(input("enter :")))
# a=[]
# for i in range(n):
#     a.append(a[input("put in the list:")])

# print(n)

# sum = 0
# while (True):
# 	userInput = input("Enter the item price or press q to quit: \n")
# 	if (userInput!='q'):
# 		sum = sum + int(userInput)
# 		print(f"Order total so far: {sum}")
# 	else:
# 		print(f"Your Bill total is {sum}. Thanks for shopping with us")
# 		break

# v=list(input())
# b=
# while v>0:
#     a=input()


# n=list(input("enter :"))
# # a=[]
# # for i in range(n):
# #     a.append(input("put in the list:"))

# print(n)


person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:{
        'organisation':'navgurukul','place':'dharamsala'
        }
    }
print(person['gender'])

print(person[4])

result = person[4]['place']

print(result) 

states_capitals = {
  'Gujarat' : 'Gandhinagar',
  'Maharashtra' : 'Mumbai',
  'Rajasthan' : 'Jaipur',
  'Bihar' : 'Patna'
  }
for state in states_capitals:
      print(state)




<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CURRICULUM</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="outer">
    <br>
    <br>
    <h1>My Resume</h1>
    <br>
    <p>
      <b> Vishal Majumdar </b><br>
Adders : H.no.-102,Sec-37,Noida,U.P-(201301)<br>
Email : Vishalm20@navgurukul.org<br>
Phone number : 9582300883
    </p>
    <hr>
    <hr>
  </div><!--end of the outer div-->
  
</body>
</html>



*{
    padding: 0px;
    margin: 0px;
}
.outer{
    width: 700px;
    height: 800px;
    border: 1px solid black;
    margin: 0px auto;
}
.outer h1{
    text-align: center;
}
p{
    font: size 20px;
}
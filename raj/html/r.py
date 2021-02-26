# # from flask import Flask,render_template,request
# # app=Flask(name)
# # app.route("/")
# # def index():
# #     return render_template("index.html")
# # app.route("/",meathod=[Post])
# def get_value():
#     First_name=requst.form["First name"]
#     Last_name=requst.form["last name"]
#     return First_name
#     # Emailid=requst.form["name"]
#     # passward=requst.form["name"]
#     # date_of_barth=requst.form["name"]
# import json
# def sign_up(First_name,Last_name,email_id,passward):
#     get_data=open("r.json","w")
#     lis=[]
#     json_data={}
#     json_data["email"]=email_id
#     json_data["passward"]=passward
#     json_data[First_name]=Last_name
#     # json_data["date"]=date
    # json_data["month"]=month
    # json_data["year"]=year
#     lis.append(json_data)
#     print(lis)
#     json.dump(lis,get_data,indent=4)
#     print("suus")
# x=input("type youe ")

# if x=="login":
#     email_id=input("ty e")
#     passward=input("type p")
#     get_data=open("r.json")
#     json_data=json.load(get_data)
#     y=[]
#     for i in json_data[0]:
#         print(i)
#         print(i["email"])
#         if i["email"]==email_id:
#             a=0
#             if i["passward"]==passward:
#                 p=0
#                 break
#             else:
#                 break
#         else:
#             continue

#     if a==0: 
#         if p==0:
#             z=open("index.html","w")
#             z.write("<html>\n")
#             z.write("<head>\n")
#             z.write("<title>\n")
#             z.write("prompt")
#             z.write("</title>\n")
#             z.write("</head>\n")
#             z.write("<body>\n")
#             z.write("<div style=width:500px;margin-top:400px;color:blue><b>login sucsfull</b></div>")
#             z.write("</body>")
#             z.write("</html")
#         else:
#             z=open("index.html","w")
#             z.write("<html>\n")
#             z.write("<head>\n")
#             z.write("<title>\n")
#             z.write("prompt")
#             z.write("</title>\n")
#             z.write("</head>\n")
#             z.write("<body>\n")
#             z.write("<div style=width:500px;margin-top:400px;color:red><b>your passward is wrong</b></div>")
#             z.write("</body>")
#             z.write("</html")
#     else:
  # z=open("index.html","w")
#             z.write("<html>\n")
#             z.write("<head>\n")
#             z.write("<title>\n")
#             z.write("prompt")
#             z.write("</title>\n")
#             z.write("</head>\n")
#             z.write("<body>\n")
#             z.write("<div style=width:500px;margin-top:400px;color:red><b>your email id is wrong</b></div>")
#             z.write("</body>")
#             z.write("</html")
#       
#       

# else:
#     First_name=input()
#     Last_name=input()
#     email_id=input()
#     passward=input()
#     sign_up(First_name,Last_name,email_id,passward)



import json
def signup(e,p):
    x=open("n.json")        
    y=json.load(x)
    m={}
    m["email"]=e
    m["passward"]=p
    y.append(m)
    a=open("n.json","w")
    json.dump(y,a,indent=4)
    z=open("index.html","r")
    z=z.read()
    print(z)
    z.write("<html>\n")
    z.write("<head>\n")
    z.write("<title>\n")
    z.write("prompt")
    z.write("</title>\n")
    z.write("</head>\n")
    z.write("<body>\n")
    z.write("<div style=width:500px;margin-top:400px;color:blue><b>signup sucsfull</b></div>")
    z.write("</body>")
    z.write("</html")
    z.close()
def login(e,p,):
    x=open("n.json")
    y=json.load(x)
    f=[]
    for i in y:
        for u in i:
            f.append(u)
    for o in f:
        zz=1     
        if i[o]==e:
            if i[o]==p:
                z=open("index.html","w")
                z.write("<html>\n")
                z.write("<head>\n")
                z.write("<title>\n")
                z.write("prompt")
                z.write("</title>\n")
                z.write("</head>\n")
                z.write("<body>\n")
                z.write("<div style=width:500px;margin-top:400px;color:blue><b>login sucsfull</b></div>")
                z.write("</body>")
                z.write("</html")
                z.close()
                zz=0
                break
            else:
                z=open("index.html","w")
                z.write("<html>\n")
                z.write("<head>\n")
                z.write("<title>\n")
                z.write("prompt")
                z.write("</title>\n")
                z.write("</head>\n")
                z.write("<body>\n")
                z.write("<div style=width:500px;margin-top:400px;color:red><b>your passward is wrong</b></div>")
                z.write("</body>")
                z.write("</html")
                z.close()
    if zz!=0:
        z=open("index.html","w")
        z.write("<html>\n")
        z.write("<head>\n")
        z.write("<title>\n")
        z.write("prompt")
        z.write("</title>\n")
        z.write("</head>\n")
        z.write("<body>\n")
        z.write("<div style=width:500px;margin-top:400px;color:red><b>your email id is wrong</b></div>")
        z.write("</body>")
        z.write("</html")
        z.close()
x=input("what you want (login,signup):  ")
if "l" in x:
    x=input("type your email id")
    y=input("type your email id passward")
    login(x,y)
else:
    x=input("type your email id")
    y=input("type your email id passward")
    signup(x,y)



# import json
# def signup(e,p,r,b,n,f,d):
#     x=open("/home/navgurukul/Desktop/P/n.json")        
#     y=json.load(x)
#     a=open("/home/navgurukul/Desktop/P/n.json","w")
#     json.dump(y,a,indent=4)
#     z=open("/home/navgurukul/Desktop/html/index.html","w")
#     z.write("<!DOCTYPE html>")
#     z.write("<html>\n")
#     z.write("<head>\n")
#     z.write("<title>\n")
#     z.write("prompt")
#     z.write("</title>\n")
#     z.write("</head>\n")
#     z.write("<body>\n")
#     z.write("<div style=width:400px;margin-top:400px><div style=color:blue><h1 style=width:400px><b>signup sucsfull</b><h1></div></div>")
#     z.write("</body>")
#     z.write("</html>")
#     z.close()
#     print("signup sucsfull")
# def login(e,p,):
#     x=open("/home/navgurukul/Desktop/P/r.json")
#     y=json.load(x)
#     q=open("/home/navgurukul/Desktop/P/n.json")
#     a=json.load(q)
#     for o in y:
#         zz=1 
#         e=o["email"]
#         p=o["passward"]
#         for i in a:
#             if i["email"]==e:
#                 zz=0
#                 if i["passward"]==p:
#                     z=open("/home/navgurukul/Desktop/html/index.html","w")
#                     z.write("<!DOCTYPE html>")
#                     z.write("<html>\n")
#                     z.write("<head>\n")
#                     z.write("<title>\n")
#                     z.write("prompt")
#                     z.write("</title>\n")
#                     z.write("</head>\n")
#                     z.write("<body>\n")
#                     z.write("<div style=width:400px;margen:auto;margin-top:400px;><div style=margin-top:400px;color:blue><h1 style=margin:auto><b>login sucsfull</b></h1></div></div>")
#                     z.write("</body>")
#                     z.write("</html>")
#                     z.close()
#                     print("login sucsfull")
#                     zz=0
#                     break
#                 else:
#                     z=open("/home/navgurukul/Desktop/html/index.html","w")
#                     z.write("<!DOCTYPE html>")
#                     z.write("<html>\n")
#                     z.write("<head>\n")
#                     z.write("<title>\n")
#                     z.write("prompt")
#                     z.write("</title>\n")
#                     z.write("</head>\n")
#                     z.write("<body>\n")
#                     z.write("<div style=width:400px;margen:auto;margin-top:400px;><div style=margin-top:400px;color:red><h1 style=margin:auto><b>your passward is wrong</b></h1></div></div>")
#                     z.write("</body>")
#                     z.write("</html>")
#                     z.close()
#                     print("your passward is wrong")
#                     break
#     if zz!=0:
#         z=open("/home/navgurukul/Desktop/html/index.html","w")
#         z.write("<!DOCTYPE html>")
#         z.write("<html>\n")
#         z.write("<head>\n")
#         z.write("<title>\n")
#         z.write("prompt")
#         z.write("</title>\n")
#         z.write("</head>\n")
#         z.write("<body>\n")
#         z.write("<div style=width:400px;margen:auto;margin-top:400px;><div style=color:red><h1 style=margin:auto><b>your email id is wrong</b><h1/></div></div>")
#         z.write("</body>")
#         z.write("</html>")
#         z.close()
#         print("your email id is wrong")
# x=input("what you want (login,signup):  ")
# if "l" in x:
#     x=input("type your email id")
#     y=input("type your email id passward")
#     login(x,y)
# else:
#     x=input("type your email id")
#     y=input("type your email id passward")
#     z=input("first name")
#     q=input("last name")
#     e=input("date of barth")
#     f=input("month of barth")
#     c=input("year of barth")
#     signup(x,y,z,q,e,f,c)



# x=input()
# pp=list(x)
# s=0
# c=[]
# e=0
# f=0
# l=0
# oo=9
# try:
#     aa=int(x)
#     print("inteser")
# except:
#     try:
#         y=x.split("+")
#         p=list(y)
#         o=p.pop(1)
#         o=list(o)
#         o=o.pop(-1)
#         if "j" == o:
#             print("complex")
#         else:
#             print(ghjkh)
#     except:
#         for i in x:
#             if i in "qwertyuiopasdfghjklzxcvbnm":
#                 s+=1
#             if i in "1234567890j":
#                 c.append(i)
#             if i in "1234567890.":
#                 f+=1
#             if x[0]=="[" and x[-1]=="]":
#                 l+=1
#                 e+=2
#                 if e<len(x)-1:
#                     if x[e]=="," and x[e-1]==",":
#                         continue
#                     else:
#                         if e!=len(x)-1:
#                             print("error of (,)")
#                             break
#             if x[0]=='{' and x[-1]=='}':
#                 print("dictenery")
#                 oo=0
#                 break
#         if s==len(pp):
#             print("string")
#         elif x[-1]=="j" and (len(c)==len(pp)):
#             print("colplex")
#         elif f==len(pp):
#             print("float")
#         elif l==len(pp):
#             print("list")
#         elif oo==0:
#             pass
#         else:
#             print("this is nothing\nBut you can make it string \nwith the help of dubble or single coot")



# import time
# p1=time.time()
# num1=[1,2]
# num2=[3,4]
# x=num1+num2
# x.sort()
# if len(x)%2==0:
#     p=len(x)//2
#     print((x[p-1]+x[p])/2)
# else:
# 	y=len(x)//2
# 	print(x[y])
# p2=time.time()
# print(p2-p1)

# d={}
# import json
# import requests
# from bs4 import BeautifulSoup as b
# rr=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in").text
# s=b(rr,'html.parser')
# b=s.find("div",class_="lister")
# v=b.find("table",class_="chart full-width")
# c=v.find("tbody",class_="lister-list")
# x=c.find_all("tr")
# v=0
# ll=[]
# for pol in x:
#     yy=x[v].find("td",class_='titleColumn').a.get_text()
#     d["name"]=yy
#     u=x[v].find("td",class_='titleColumn').span.get_text()
#     u=u[1:-1]
#     d["year"]=u
#     z=x[v].find("td",class_="ratingColumn imdbRating").strong.get_text()
#     d["rating"]=z
#     bb=x[v].find("td",class_='titleColumn')
#     bb=bb.find("a")["href"]
#     d['link']=bb
#     v+=1
#     ooo=open("n.json","w")
#     ll.append(d)
#     json.dump(ll,ooo,indent=4)
#     d={}


# d={}
# dd={}
# pp=[]
# lk=[]
# import json
# o=open("n.json")
# l=json.load(o)
# x=[]
# for i in l:
#     x.append(i["year"])
# x=set(x)
# x=list(x)
# x.sort()
# for x in x:
#     for i in l:
#         if x==i['year']:
#             dd["name"]=i["name"]
#             dd["year"]=i["year"]
#             dd["rating"]=i["rating"]
#             dd["link"]=i["link"]
#             pp.append(dd)
#             dd={}
#     d[x]=pp
#     o=open("r.json","w")
#     lk.append(d)
#     json.dump(lk,o,indent=4)
#     d={}
#     pp=[]

# d={}
# dd=[]
# li=[]
# import json
# o=open("r.json")
# l=json.load(o)
# xx=1950
# for i in l:
#     for kl in i:
#         for val in i[kl]:
#             if int(kl)>=xx and int(kl)<xx+10:
#                 li.append(val)
#             else:
#                 d[str(xx)]=li
#                 op=open("n.json","w")
#                 dd.append(d)
#                 json.dump(dd,op,indent=4)
#                 xx+=10
#                 d={}
#                 li=[]
#                 li.append(val)

# di={}
# d2={}
# import json
# import requests
# from bs4 import BeautifulSoup as b
# o=open("n.json")
# ll=[]
# lk=[]
# pol=[]
# l=json.load(o)
# for i in l:
#     for ii in i.values():
#         for x in ii:
#             ll.append(x["link"])
#             lk.append(x["name"])
# for i in ll:
#     for vb in lk:
#         link="https://www.imdb.com"+str(i)+"?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=6NWFW74GS34D14G9RMTQ&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_"
#         rr=requests.get(link).text
#         s=b(rr,'html.parser')
#         ss=s.find("div",id="main_bottom")
#         aa=s.find("div",class_="article",id="titleDetails")
#         aa=aa.find_all("div",class_="txt-block")
#         ju=0
#         for  bb in aa:
#             if  (aa[ju].find("h4").get_text())=="Language:":
#                 a=bb.find('a').get_text()
#                 break
#             ju+=1
#         lkp=0
#         for nh in aa:
#             if aa[lkp].find("h4")==None:
#                 tt="time is not given"
#                 break
#             elif (aa[lkp].find("h4").get_text())=="Runtime:":
#                 tt=aa[lkp].find("time").get_text()
#                 break
#             lkp-=1
#         xc=s.find("div",class_="credit_summary_item").a.get_text()
#         d2["direacter"]=xc
#         d2["language"]=a.split(" ")
#         d2["time"]=tt
#         di[vb]=d2
#         o=open("r.json","w")
#         pol.append(di)
#         json.dump(pol,o,indent=4)
#         di={}
#         d2={}
#         lk.remove(vb)
#         break

# import time
# from selenium.webdriver.common.keys import Keys 
# import selenium.webdriver.common.keys
# import threading
# from selenium import webdriver
# from bs4 import BeautifulSoup as b
# PATH="/home/navgurukul/Downloads/chromedriver"
# time.sleep(2)
# driver=webdriver.Chrome(PATH)
# driver.get("https://www.flipkart.com/home-entertainment/pr?sid=ckf&otracker=categorytree")
# time.sleep(2)
# time.sleep(4)
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
# x=driver.
# bea=b(x,"html.parser")
# # data=bea.find("div",class_="E2-pcE _3zjXRo")
# data=bea.find("div",class_="E2-pcE _1q8tSL")
# print(data)
# l_data=data.find_all("div",class_="_2pi5LC col-12-12")
# print(len(l_data))



# import requests
# from bs4 import BeautifulSoup as b
# r=requests.get("https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DSony").text
# rr=b(r,"html.parser")
# x=rr.find("div",class_="E2-pcE _3zjXRo")
# p=x.find_all("div",class_="_2pi5LC col-12-12")
# print(len(p))
# p.pop(0)
# p.pop(0)
# p.pop(-1)
# p.pop(-1)
# for i in p:
#         a=i.find("div",class_="_2kHMtA")
#         print(i)
#         link=a.find("a")["href"]
#         aaa=a.find("div",class_="_3pLy-c row")
#         d=aaa.find("div",class_="_2pi5LC col-12-12")
#         a=d.find("div",class_="_4rR01T").get_text()
#         print(a)
#         q=d.find("div",class_="gUuXy-")
#         q=q.find("div",class_="_3LWZlK").get_text()
#         print(q)
#         w=d.find("div",class_="fMghEO")
#         w=w.find_all("li",class_="rgWa7D")
#         for i in w:
#                 aa=i.get_text()
#                 print(aa)
#         z=aaa.find("div",class_="col col-5-12 nlI3QM")
#         z=z.find("div",class_="_30jeq3 _1_WHN1").get_text()
#         print(z)
#         break


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
# def ox(upo,dic,qu,d,aaa,link):
#         w=d.find("div",class_="fMghEO")
#         w=w.find_all("li",class_="rgWa7D")
#         for i in w:
#                 aa=i.get_text()
#                 qu.append(aa)
#         dic["qualites"]=qu
#         qu=[]
#         z=aaa.find("div",class_="col col-5-12 nlI3QM")
#         z=z.find("div",class_="_30jeq3 _1_WHN1").get_text()
#         z=str(z.replace("\u20b9","Rs"))
#         dic["amount"]=z
#         rr=requests.get("https://www.flipkart.com"+str(link)).text
#         bs=b(rr,"html.parser")
#         aa=bs.find("div",class_="_1YokD2 _3Mn1Gg col-8-12")
#         if aa==None:
#                 pass
#         ss=aa.find("div",class_="_1YokD2 _3Mn1Gg")
#         ad=ss.find_all("div",class_="_1AtVbE col-12-12")
#         for ii in ad:
#                 di=ii.find("div",class_="_3nkT-2")
#                 if di!=None:
#                         dii=ii.find("div",class_="_3cFJ8l").get_text()
#                         if dii=="Description":
#                                 II=di.find("div",class_="_2o-xpa")
#                                 po=II.find("div",class_="_1mXcCf RmoJUa")
#                                 if po==None:
#                                         po=ii.find("div",class_="_1mXcCf").get_text()
#                                         dic[str(dii)]=[po]
#                                         break
#                                 else:
#                                         p=po.find("p")
#                                         if p==None:
#                                                 ol=po.get_text()
#                                                 dic[str(dii)]=[ol]
#                                                 break
#                                         else:
#                                                 po=p.get_text()
#                                                 dic[str(dii)]=[po]
#                                         break
#                 dic['link']=link
#                 hg=open("n.json","a")
#                 upo.append(dic)
#                 json.dump(upo,hg,indent=4)
#                 dic={}
#                 qu=[]   
#                 time.sleep(1)
# def cod(url):
#         upo=[]
#         dic={}
#         qu=[]
#         print(url[0])
#         r=requests.get("https://www.flipkart.com"+str(url)).text
#         rr=b(r,"html.parser")
#         tyur=rr.find("div",class_="_3FqKqJ")
#         rrr=tyur.find("div",class_="E2-pcE _3zjXRo")
#         p=rrr.find_all("div",class_="_2pi5LC col-12-12")
#         print(len(p)-4)
#         p.pop(0)
#         p.pop(0)
#         p.pop(-1)
#         p.pop(-1)
#         for i in p:
#                 a=i.find("div",class_="_2kHMtA")
#                 link=a.find("a")["href"]
#                 aaa=a.find("div",class_="_3pLy-c row")
#                 d=aaa.find("div",class_="col col-7-12")
#                 aas=d.find("div",class_="_4rR01T").get_text()
#                 print(aas)
#                 dic["model"]=aas
#                 q=d.find("div",class_="gUuXy-")
#                 if q==None:
#                         dic["reating"]="no reating"
#                         ox(upo,dic,qu,d,aaa,link)
#                 else:
                        
#                         q=q.find("div",class_="_3LWZlK").get_text()
#                         dic["reating"]=q                                   
#                         ox(upo,dic,qu,d,aaa,link)
# yui=[]
# for url in pol:
#         t1=multiprocessing.Process(target=cod,args=[str(url)])
#         t1.start()
#         yui.append(t1)
# for threds in yui:
#         threds.join()       
# 
# d={}
# def x(a):
#         for i in range(10):
#                 o=open("r.json")
#                 df=json.load(o)
#                 o=open("r.json","w")
#                 d[a]=str(i)
#                 df.append(d)
#                 json.dump(df,o,indent=4)
# a=['1',"2",'3']
# for i in a:
#         t1=multiprocessing.Process(target=x,args=i)
#         t1.start()









# 
# 
#                      
# # time.sleep(1)
# # yui=[]
# for url in pol:
#         cod(str(url))
# # t1=multiprocessing.Process(target=cod,args=[pol[0]])
# # t1.start()
#         # time.sleep(1)
#         # yui.append(t1)
# # for threds in yui:
# #         threds.join()




# # import time
# # import multiprocessing

# # def x(b):
# #         for i in range(10):
# #                 print(str(i)+b)
# #                 time.sleep(1)      
# # t1=multiprocessing.Process(target=x,args=["hi"])
# t2=multiprocessing.Process(target=x,args=["hallo"])
# t1.start()
# t2.start()
# 6 mem
# D.horrner
# 10th 2009
# 12
# 2014
# job 2-4,5
# furture goals-dr.
#  second offtion teacher
#  1
#  father gnerl-per day 4000
#  mother h
#  yonger 9
#  second 12
#  area-ngo rista (give )

# x=input()
# o=0
# p=[]
# lj=[]
# c=0
# x=list(x)
# def cv(x,p,lj=0,l=[]):
#     while "(" in x:
#         for i in x:
#             if i==")":
#                 x.remove(i)
#                 x.remove("(")
#                 lj=lj-1
#                 while lj!=0:
#                     l.append(x[lj-lj])
#                     x.remove(x[0])
#                     lj-=1
#                 y(l,p)
#             else:
#                 lj+=1
#     if len(x)==0:
#         print(sum(p),"e")
#     else:
#         l=x
#         y(l,p)
    
    

# l=[]
# def y(y,p,c=0):
#     while "/" in y:
#         for i in y:
#                 if i=="/":
#                     print(y)
#                     d=int(y[c-1])/int(y[c+1])
#                     y.remove(y[0])
#                     y.remove(y[0])
#                     y.remove(y[0])
#                     l.append(d)
#                     p.append(l[0])
#                 c+=1
#     if len(y)==0:
#         cv(y,p)
#     else:
#         o(y,p)
    
# def o(y,p,c=0):
#     while "*" in y:
#         for i in y:
#             if i=="*":
#                 d=int(y[c-1])*int(y[c+1])
#                 y.remove(y[0])
#                 y.remove(y[0])
#                 y.remove(y[0])
#                 l.append(d)
#             c+=1
#     if len(y)==0:
#         p.append(l[0])
#         cv(y,p)
#     else:
#         s(y,p)
# def s(y,p,c=0,l=[]):
#     while "+" in y:
#         for i in y:
#             if i=="+":
#                 d=int(y[c-1])+int(y[c+1])
#                 y.remove(y[0])
#                 y.remove(y[0])
#                 y.remove(y[0])
#                 l.append(d)
#             c+=1
#     if len(y)==0:
#         p.append(l[0])
#         cv(y,p)
#     else:
#         m(y,p)

# def m(y,p,c=0):
#     while "-" in y:
#         for i in y:
#             if i=="-":
#                 d=int(y[c-1])-int(y[c+1])
#                 y.remove(y[0])
#                 y.remove(y[0])
#                 y.remove(y[0])
#                 l.append(d)
#             c+=1
#     if len(y)==0:
#         p.append(l[0])
#         cv(y,p)
#     else:
#         cv(y,p) 
# cv(x,p)

# [1+2*(3/3)]
# [1+2*1]
# [1+2]
# [3]

# def y(x,q=0,c=0,b=0):
    # w=[]
    # print(x)
    # if len(x)>=2:
    #     if "(" in x:
    #         for i in x:
    #             if i==")":
    #                 q=q-1
    #                 b=q
    #                 while  True:
    #                     if x[b]!="(":
    #                         b-=1
    #                     else:
    #                         bb=b
    #                         b+=1
    #                         break
    #             else:
    #                 q+=1
    #         while x[b]!=")":
    #             w.append(x[b])
    #             b+=1
    #             print(x[b])
    #         print(bb,"kq",w)
    #         x.remove(")")
    #         x.pop(bb)
    #         print(x,"234rt")
    #         print(w)
    #         jh=div(w)
    #         op=bb
    #         while bb!=q:
    #             print(x.pop(op))
    #             bb+=1
    #         if len(x)==0:
    #             print(w.pop(0))
    #             if len(w)==1:
    #                 return w[0]
    #             else:
    #                 print(w,"l")
    #                 w=div(w)
    #                 print(w)
    #                 if len(w)==1:
    #                     return w[0]
    #         else:
    #             x.insert(op,"*")
    #             x.insert(op+1,jh)
    #             print(x,"0000000000000")
    #             y(x)

    # else:
    #     print(x[0]) 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# x=input()
# x=x.split(" ")
# def y(x,q=0,lk=""):
#     w=[]
#     if "(" in x:
#         for i in x:
#             if i==")":
#                 x.pop(q)
#                 q-=1
#                 while x[q]!="(":
#                     w.insert(0,x[q])
#                     x.pop(q)
#                     q-=1
#                 break
#             else:
#                 q+=1
#         x.pop(q)
#         re=div(w)
#         if len(x)==0:
#             print(w[0])
#         else:
#             if x[q-1] not in ["+","-","*","/"]:
#                 x.insert(q,"*")
#                 if x[0]!="*":
#                     x.insert(q+1,re)
#                     y(x)
#                 else:
#                     x.insert(q+1,re)
#                     x.pop(0)
#                     y(x)
#             else:
#                 x.insert(q,re)
#                 if len(x)==1:
#                     print(x[0])
#                 else:
#                     y(x)
#     else:
#         re=div(x)
#         print(re)
# def div(w,c=0):
#     if "/" in w:
#         while "/" in w:
#             for i in w:
#                     if i=="/":
#                         d=float(w[c-1])/float(w[c+1])
#                         w.pop(c-1)
#                         w.pop(c-1)
#                         w.pop(c-1)
#                         w.insert(c-1,d)
#                     else:
#                         c+=1
#     mn=mul(w)
#     return mn 
# def mul(w,c=0):
#     if "*" in w:
#         while "*" in w:
#             for i in w:
#                 if i=="*":
#                     d=float(w[c-1])*float(w[c+1])
#                     w.pop(c-1)
#                     w.pop(c-1)
#                     w.pop(c-1)
#                     w.insert(c-1,d)
#                     c=0
#                     break
#                 else:
#                     c+=1
#     mn=plu(w)
#     return mn
# def plu(w,c=0):
#     if "+" in w or "-" in w:
#         while "+" in w or "-" in w:
#             for i in w:
#                 if i=="+" or i=="-":
#                     c=1
#                     if w[c]== "+":
#                         d=float(w[c-1])+float(w[c+1])
#                     elif w[c]=="-":
#                         d=float(w[c-1])-float(w[c+1])
#                     w.pop(c-1)
#                     w.pop(c-1)
#                     w.pop(c-1)
#                     w.insert(c-1,d)
#                     c=0
#                 else:
#                     c+=1
#     return w[0]
# y(x)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# a=1
# sum=0
# while a<=100:
#     sum=sum+a
#     print (sum)
#     a+=

# a=1
# while a<100:
#     if a%2==0:
#         print(-a,a-1)
#     a+=1



# a=1
# while a<=100:
#     if a%2==0:
#         print(a)
#     else:
#         print(a)
#         if a==99:
#             a-=97
#             continue
#     a+=2


# x= input()
# x=x.split(" ")
# x.sort()
# print(x)
# op=""
# kl=[]
# for i in m:
#     m.remove(i)
#     if i in m:
#         kl.append(i)
#         m.append(i)
#         if i not in kl:
#             i.append(i)
# print(kl)
# [l l l m k b h j m]


x=input()
if len(x)>=8 and len(x)<=16:
    if "!" in x or "@" in x or "#" in x or "$" in x or "%" in x or "^" in x or "&" in x:
        if  "1" in x or "2" in x or "3" in x or "4" in x or "5" in x or "6" in x or "7" in x or "8" in x or "9" in x or "0" in x:
            if "q" in x or "w" in x or "e" in x or "r" in x or "t" in x or "y" in x or "u" in x or "i" in x or "o" in x or "p" in x or "a" in x or "s" in x or "d" in x or "f" in x or "g" in x or "h" in x or "j" in x or "k" in x or "l" in x or "z" in x or "x" in x or "c" in x or "v" in x or "b" in x or "n" in x or "m" in  x:
                if "Q" in x or "W" in x or "E" in x or "R" in x or "T" in x or "U" in x or "I" in x or "O" in x or "P" in x or"A" in x or "S" in x or "D" in x or "F" in x or "G" in x or "H" in x or "J" in x or "K" in x or "L" in x or "Z" in x or "X" in x or "C" in x or "V" in x or "B"  in x or "N" in x or "M" in x:
                    print("strong passward")
                else:
                    print("upper")
            else:
                print("lower")
        else:
            print("num")
    else:
        print("spassel")
else:
    print("len")

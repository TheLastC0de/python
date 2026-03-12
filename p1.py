#mylist = ["Prashant", "Ashish","komal","ankush",77,"sandip",60.52,"prashant"]
#print(mylist)
#print(type(mylist))
#print(mylist[0])
#print(mylist[1])
#print(mylist[2])
#print(mylist[-1])
#print(mylist[2:5])
#print(mylist[:5])
#print(mylist[1:])
#print(mylist[1:8:2])
#print(mylist[:])
#print(mylist[::-1])
#print(" ")
#copy function 
#newlist = mylist.copy()
#print(newlist)
#inserting element
#mylist.append("harsh")
#mylist.append("laxman")
#print(mylist)

#mylist = [["Prashant", "Jha"],['85,56'],[440022,'yyy']]
#print("example of multidimensional list:")
#print(mylist)
#print(mylist[row][col])
#print(mylist[0][0])
#print(mylist[0][1])
#print(mylist[1][0])
#print(mylist[2][0])
#print(mylist[2][1])

#list1=["prashant","jha"]
#print(list1*2)
#list2=[50,25.50]
#print(list1+list2)

#list2=[50,25.50,"prashant"]
#list2.clear
#print(list2)

#mylist=[44,22,66,7,45,88]
#mylist.sort(reverse=True)
#print(mylist)

#math=50
#phy=50
#print(id(math))
#print(id(phy))

#looping 2 types of special operator membership operator: 2 type:
#1. in
#2. not in
#name = 'parshant'
#print('Z' not in name)
#for i in range(1,11):
#    print(i*2," ",i*3," ",i*4)

#no=int(input("Enter any digit: "))
#if no>0:
#    print('positive')
#if no<0:
#    print("negative")
#if no==0:
#    print('zero')

#day=input("Enter a day: ")
#if day == "monday" or "tue" or 'wed' or 'thu' or 'fri':
#   print('workday')
#if day == 'sun' or 'sat':
#    print('weekend')
#else:
#    print("enter valid day")

#math=int(input("Enter marks: "))
#chem=int(input("Enter marks: "))
#phy=int(input("Enter marks: "))
#tot=math+chem+phy
#print("total marks: ", tot)
#perc=tot/3.0
#print("Percentage",perc)
#if perc>=60:
#    print("eligible")
#else:
#    print('not eligible')

#wop to accept 5 diff value in 5 diff variable and check max value 
#and print by using simple if statement
#a=int(input("Enter num: "))
#b=int(input("Enter num: "))
#c=int(input("Enter num: "))
#d=int(input("Enter num: "))
#e=int(input("Enter num: "))
#maximum=max(a,b,c,d,e)
#print(maximum)

#per = int(input("enter your % "))
#if per>= 90:
#    print("grade A")
#elif per>= 80 and per<90:
#    print("grade A")
#elif per>= 60 and per<80:
#    print("grade A")
#else:
#    print("fail")

#DICTIONARY DATATYPE
#mydict = {
#    "name": "prashant",
#    "profession": "developer",
#    "empid":1001
#}
#print(mydict)
#print(type(mydict))

# mydict= {
#     101: "prashant",
#     102: "ashish",
#     "103": "mohini",
#     "104": "trivani",
#     101: "ashish",
#     104: "ashish"
# }
#print(mydict)
#a=mydict[102]
#print(a)
#mydict[102]="peter"
#print(mydict)
#for x in mydict.values():
#    print(x) 
#for x, y in mydict.items():
#    print(x,y)
#mydict["mobile_no"]=345634545
#print(mydict)
#mydict.pop(101)
#print(mydict)
# name="prashantjha"
# print(name[0])
# print(name[2])
# print(name[0])
# print(name[0])
# print(name[0])

# from shlex import join


# s="help4code is a best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

# s="prashant","ashish",'sanidip'
# m='|'.join(s)
# print(m)

# s="Python is a high level peogramming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print('subjects marks')
# phy=50
# chem=60
# math=70
# print("physics ={} chem={} math={}".format(phy,chem,math))
# print("physics={0} chem={1} math={2}".format(phy,chem,math))
# print("physics ={x} chem={y} math={z}".format(x=phy,y=chem,z=math))
# total=phy+chem+math
# print("total marks = {}",f"{total}")
# print("Roll no= ", "7".zfill(4))

# print('prashantjha777'.isalnum())
# print('prashantjha'.isalpha())
# print('777f'.isdigit())
# print('sasasasa'.islower())
# print(''.islower())
# print("My Name Is Prashant".istitle())
# print(''.istitle())
# print(''.isspace())
# print('Hello'.startswith("He"))
# print("Hello".endswith("lo"))

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

name="prashant"
for i in name:
    print(i)
# i=1
# while i<=5:
#     print(i)
#     i=i+1
# 
# username=''
# password=''
# while username!='admin' and password!='hello':
#     username=input("enter username: ")
#     password=input("enter password: ")

# n=int(input('enter number: '))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("the sum of first ",n,"numbers is: ",sum)

# name='prashant'
# newname=''
# for i in name:
#     if i not in newname:
#         newname+=i
#         print(newname)

# name='prashant'
# rev=''
# for i in name[::-1]:
#     rev+=i
# print(rev)

# mycart=[10,20,30,200,800,60,700]
# for i in mycart:
#     if i>400:
#         print("this is mycart purchased item")
#         continue
#     print(i)

#palindrome
# name=input("enter a name")
# if name==name[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

# char1=input("enter a word: ")
# char2=input("enter a word: ")
# x=''
# for i in char1:
#     if i not in char1:
#         x+=i
#         break
# for j in char2:
#     if x not in char2:
#         print("it is an anagram")
#     else:
#         print("not an anagram")

#remove key pairs from dictionary 
#sample input dictionary: {"name":"Alice","age":"30"} key "age"

#check if a key exists in a dictionary
#sample input dictionary: {"name":"Alice","age":"30"} key "age"

#iterate over dictionary keys and values 
#sample input dictionary: {"name":"Alice","age":"30"} 

#merge two dictionary

# # #nested for loop
# n=int(input("enter number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
    
n=int(input("enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()
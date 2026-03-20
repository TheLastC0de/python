# fruit_list1 = ['apple','berry','cherry','papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'guava'
# fruit_list3[1] = 'mango'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'guava':
#         sum += 1
#     if ls[1] == 'mango':
#         sum += 20
# print(sum) #ans 22

# def f(i, values = []):
#     values.append(i)
#     print(values)  
# f(1)
# f(2)
# f(3)

# def func(value, values):
#     var=1
#     values[0] = 44
# t=3
# V=[1,2,3]
# func(t,V)
# print(t, V[0])

# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print(dict[_])

fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
addone('apple')
addone('banana')
addone('apple')
print(len(fruit))
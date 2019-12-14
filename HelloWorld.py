
'''
print("Hello World")
print("We are currently using github")

import random
def cd_gen(times = 1):
    for x in range(times):
        a =(random.random())
        b = (random.randint(40,100))

        c = (round(a + b, 2))

        cd_list = ["N", "E", "S", "W", "SE", "SW", "NW",  "NE"]

        cd = random.choice(cd_list)
        return(str(c) + "°" + cd)
cd_gen(5)
print("Food is currently being sent to",cd_gen(1))
'''


# QUESTION 1
'''
def rotate(a, b, c):
    list1 = [a, b, c]
    x = (list1.pop(0))
    list1.append(int(x))
    return (list1)
#list2 = list1.append(x)
#print(list2)
print(rotate(1,2,3))
'''

# QUESTION 4
'''
def LastTwo(string):
    string = list(string)
    x = string.pop(-2)
    string.append(x)
    print("".join(string))
LastTwo("cat")
'''

# QUESTION 3
'''
def ShiftLeft(intlist):
    intlist = list(intlist)
    lst = []
    for x in intlist:
        lst.append(int(x))
    x = lst.pop(0)
    lst.append(x)
    print(lst)
ShiftLeft('12433423')
'''

# QUESTION 2
'''
a = [1,2,3,4,5,3,4,3]

y = 0
for x in a:
    if x == 3:
        y += 1
        index = a.index(x)
        print(index)

print(y)
'''
'''
#hi
my_list = [10,2,3,5,2,1,6,3,5,2,2]
a = 2# element to be found
for x in range(len(my_list)):#traversing through length of the list
    if my_list[x] == a:
        print(x)
'''

a = [1, 2, 3, 4, 100, 6]
if len(a)%2 == 1:
    y = int(len(a)/2) + 1
    print(a[y - 1])
else:
    if len(a)% 2 == 0:


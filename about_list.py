#python Lists
first_list=[True,"my name:rajya","age:20","phone:888632145","mail:abc@xyz",1,2,3,4,5,6,7,8,3.0]
second_list= list(("hai","hello","good night"))
third_list=[1,2,3]
fourth_list=[8,2,9,4,6,1,3,55,44,77]
print("1:",second_list)
print(first_list)
print("2:",len(first_list))
print("3:",type(first_list))
print("4:",first_list[1],second_list[1],first_list[-1],first_list[2:5])
print("5:",first_list[:4])
print("6:",first_list[-4:-1])
if "hello" in second_list:
    print("7:","yes hello is there in second_list")
first_list[0]=False
print("8:",first_list[0])
first_list[1:3]=[1,2,3]
print("9:",first_list[1:4])
first_list.insert(0,"my self rajya")
print("10:",first_list[0])
second_list.append("apple")
print("11:",second_list[-1])
third_list.extend(second_list)
print("12:",third_list)
#we can extend the list by tuple dictionary aslo
first_list.remove("mail:abc@xyz")#The remove() method removes the specified item.
print("13:",first_list)
first_list.pop(0)#The pop() method removes the specified index.
print("14:",first_list)
#If you do not specify the index, the pop() method removes the last item.
third_list.clear()
"""
The clear() method empties the list.

The list still remains, but it has no content.
"""
print("15:",third_list)
#Loop-Lists
"""
for i in second_list:#You can loop through the list items by using a for loop:
    print("16:",i,end=" ")
[print("17:",a,end=" ") for a in second_list]#List Comprehension offers the shortest syntax for looping through lists:
"""
"""
list comprehension
newlist = [expression for item in iterable if condition == True]
"""
fourth_list.sort()#reverse=True|False
print("18:",fourth_list)#To sort descending, use the keyword argument reverse = True:
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#The reverse() method reverses the current sorting order of the elements.
fourth_list.reverse()
print("19:",fourth_list)
#Make a copy of a list with the copy() method:
A=first_list+second_list #One of the easiest ways are by using the + operator.
print("20:",A)
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""






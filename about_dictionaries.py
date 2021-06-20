#Python_Dictionary:Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Duplicate values will overwrite existing values:
#String, int, boolean, and list data types:
"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
first_dict={"first":"reliance","second":"samsung","third":"motorola","forth":"honar","fifth":"poco"}
print("1:",first_dict) #Create and print a dictionary:
print("2:",first_dict["first"]) #Duplicates Not Allowed
print("3:",type(first_dict)) #String, int, boolean, and list data types:
x=first_dict["second"]
print("4:",x) #Get the value of the "model" key:
print("5:",first_dict.get("fifth"))#Get the value of the "model" key:
print("6:",first_dict.keys()) #Get a list of the keys:
s=first_dict["sixth"]="iphone" #Add a new item to the original dictionary, and see that the keys list gets updated as well:
print("7:",first_dict["sixth"])
first_dict["sixth"]="oneplus"
print("8:",first_dict["sixth"]) #Make a change in the original dictionary, and see that the values list gets updated as well:
print("9:",first_dict.items()) #Get a list of the key:value pairs
if "sixth" in first_dict:
    print("10:","yes it is  there in dictionary")
first_dict.update({"sixth":"samsung"})
print("11:",first_dict) #Update the "year" of the car by using the update() method:
first_dict.pop("sixth") #The pop() method removes the item with the specified key name:
print("12:",first_dict)
#del first_dict #The del keyword can also delete the dictionary completely:
#print("13:",first_dict)
#first_dict.clear()
#print("14:",first_dict)
for x in first_dict: #Print all keys in the dictionary, one by one:
    print("15:",x)
for x in first_dict: #Print all values in the dictionary, one by one:
    print("16:",first_dict[x])
for x in first_dict.values(): #You can also use the values() method to return values of a dictionary:
    print("17:",x)
for x in first_dict.keys(): #You can use the keys() method to return the keys of a dictionary:
    print("18",x)
for x,y in first_dict.items():
    print("19:",x,y)







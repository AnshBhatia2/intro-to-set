samples = [894, "sign", 70, "sunny"]
print(samples)
print(samples[3])

#converting list to set
sample_set = set(samples)
print(sample_set)
#set does not take index numbers
#print(sample_set[2])

#even though we cant use index numbers we can check if an element exists or not
if "cloudy" in sample_set:
    print("yes")

else:
    print("no")

#creating an empty set
mylist = []
myset = set(mylist)

#or
my_set = set([])

#adding an element to a set
my_set.add("map")
my_set.add(8)
my_set.add("math")
my_set.add(402)
my_set.add("payment")
my_set.add(13)
print(my_set)

#removing items from the set
my_set.remove(402)
#remove function gives error if item to delete is not present in set
#my_set.remove("srh")

#discard function does not give error if element is not there
my_set.discard("payment")
my_set.discard("RR")
print(my_set)

#set operations
seta = {457,5,45,6,84,636,87}
setb = {457,6,87,678,78,21,1}

#1 union operation
aunionb = seta.union(setb)
print(aunionb)
#or
print(seta | setb)

#2 intersection operation
aintersectionb = seta.intersection(setb)
print(aintersectionb)
#or
print(seta & setb)

#3 difference operation
adifferenceb = seta.difference(setb)
print(adifferenceb)
print(setb.difference(seta))
#or
print(seta - setb)

#4 symmetric difference operation
print(seta.symmetric_difference(setb))
#or 
print(seta ^ setb)

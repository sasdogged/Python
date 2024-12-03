my_list = []
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(1, 15)
print(my_list)

another_list = [50,60,70]

my_list.extend(another_list)
print("After extending:", my_list)

my_list.remove(70)
print("After removing:", my_list)

my_list.sort()
print("In ascending order:",my_list)

index = my_list.index(30)
print("The index of 30:", index)

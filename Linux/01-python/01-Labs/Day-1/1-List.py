# List 

x = 'Alaa'
my_list = [x, 1, 5.4, 'momo', 0.7]
print(my_list)
print(my_list[3])
print(my_list[4])

#change in element of list

my_list[1] = "safa"
print(my_list)

#index range
print(my_list[-1])# 0.7
print(my_list[-2])
print(my_list[-4])

print("************************************")
print(my_list[0:4:1])
print(my_list[-1:-4:-1])# 

print("************************************")
print(my_list[:4:1])
print(my_list[:-4:-1])

print("************************************")
print(my_list[0::1])
print(my_list[-1::-1])

print("************************************")
print(my_list[0:4:])
print(my_list[-1:-4:])# [ empty ]



print("\n***************  append data   *******************")
x = "ITI"
Y = "567575I67TI5462" 
my_list.append(x) # append x to end of list
my_list.append(Y)
print(my_list)

print("\n***************  extend data   *******************")
my_list.extend(Y) # append all elements of Y to list
print(my_list)

print("\n***************  insert data   *******************")
x = "zipy"
my_list.insert(0, x) # insert x at index 1
my_list.insert(0, x)
my_list.insert(0, x)
print(my_list)

print("\n***************  remove data   *******************")
my_list.remove(x) # remove first occurance of x from list
my_list.remove("5")
print(my_list)

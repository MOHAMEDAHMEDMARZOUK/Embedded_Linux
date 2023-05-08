'''
num1 = 12 
print(num1)
num2 = "hdshjshjsjhjs" 
num1 = "kled" 
print(""num1)
print(num2)
print("mohamed marzok ESWE ")
print("graduation year :: 2022")
print("age year :: 1999")
print("Bachelor's degree in Communication and Electronics Engineering ")
print("Cumulative Grade: Excellent with honors (Top of my class) :: ")
print("2017 – 2022 | Cairo, Egypt")


MyName = input ("Please Enter your name ") 
print ("My name is %d" +((MyName)))
print ("My name is %d" %(int(MyName)))
print ("My name is " ,int(MyName))
print (MyName) '''

'''
# taking two inputs at a time  
a, b, c = input("Enter three values: ").split(" ",3)  
print("val1: ", a)  
print(type(a))
a = int (a)
print(type(a))
print("val1: ", b)  
print("val1: ", c)  '''

# List 

'''

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
'''

#tuple
'''
# create tuple 
tuple_nme = ("kjooo",)
print(tuple_nme)
print(len(tuple_nme))
print(type(tuple_nme))


# print tuple 
tuple_nme = ("kjooo",67,768.99,'mozo',"apple", "banana", "cherry")
print(tuple_nme)
print(len(tuple_nme))
print(type(tuple_nme))


# to print length of tuple 
print(len(tuple_nme))
print(tuple_nme[1])

#tuple_nme[1] = 1  # will produce error tuple is a constant 
'''

#range
'''
# creaate range 
x = range(0,100,1)
print(x)

for n in x:
   print(n)
   
   '''
   
#dic 

dic_name = { "momo" : 24 ,
             "hger" : 27 ,
             "bob"  :61  ,}

print(dic_name)
print(len(dic_name))

#to dd element

dic_name["kso"] = 7.5

print(dic_name)
print(len(dic_name))
print(dic_name["hger"])

dic_name["kso"] = 10
print(dic_name)

print("************************************")
print("************************************")
print("************************************")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(len(thisdict))
print(thisdict["colors"])
print(thisdict["colors"][0])
print(thisdict["colors"][1])
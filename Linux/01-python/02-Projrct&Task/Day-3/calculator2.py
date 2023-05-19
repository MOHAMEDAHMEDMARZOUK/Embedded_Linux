import math

while(True):
	print("Please enter the type of Number ")
	print('''The options:
1-HEX
2-DEC
3-OCT
4-BIN''')
	type_number=input(">")
	print("\nPlease choose the operation")
	print('''The options:
1.ADD    2.SUB    3.MUL    4.DIV       5.MODULS    6.NOT    
7.AND    8.OR     9.XOR    10.POWER    11.SQRT     12.LOG   13.LN ''')
	operation = input(">")

	if(type_number=='HEX'):
		if(operation=='ADD'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
		
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
		
			result=num1+num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='MUL'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
		
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
		
			result=num1*num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
		
		elif(operation=='DIV'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1/num2
			print("\nthe result in DEC = ",result)
		
		elif(operation=='MODULS'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1%num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
		
		elif(operation=='AND'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1&num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
		
		elif(operation=='OR'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1|num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='XOR'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1^num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='POWER'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter the power number : ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=pow(num1,num2)
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='NOT'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=~num1
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SQRT'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=math.sqrt(num1)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LOG'):
			hex_str = input("Please enter the number : ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter the base: ")
			num2 = int(hex_str2, 16)
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=math.log(num1,num2)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LN'):
			hex_str = input("Please enter the number : ")
			num1 = int(hex_str, 16)
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=math.log(num1)
			print("\nthe result in DEC = ",result)
	
		else:
			print("Not valid operation")

	elif(type_number=='DEC'):
		if(operation=='ADD'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1+num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SUB'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1-num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='MUL'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1*num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='DIV'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1/num2
			print("\nthe result in DEC = ",result)
			
		elif(operation=='MODULS'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1%num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='AND'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1&num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='OR'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1|num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='XOR'):
			num1 = int(input("Please enter number 1: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter number 2: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1^num2
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='POWER'):
			num1 = int(input("Please enter the number: "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter the power number: "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=pow(num1,num2)
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))	
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='NOT'):
			num1 = int(input("Please enter number : "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=~num1
			print("\nthe result in DEC = ",result)
			print("the result in HEX = ",hex(result))
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SQRT'):
			num1 = int(input("Please enter number : "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=math.sqrt(num1)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LOG'):
			num1 = int(input("Please enter number : "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			num2 = int(input("\nPlease enter the base number : "))
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=math.log(num1,num2)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LN'):
			num1 = int(input("Please enter the number : "))
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=math.log(num1)
			print("\nthe result in DEC = ",result)
	
		else:
			print("Not valid operation")

	elif(type_number=='OCT'):
		if(operation=='ADD'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1+num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SUB'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1-num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='MUL'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1*num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='DIV'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1/num2
			print("\nthe result in DEC = ",result)
			
		elif(operation=='MODULS'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1%num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='AND'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1&num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='OR'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1|num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='XOR'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=num1^num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='POWER'):
			hex_str = input("Please enter the number: ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter the power number: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=pow(num1,num2)
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='NOT'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=~num1
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SQRT'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			result=math.sqrt(num1)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LOG'):
			hex_str = input("Please enter the number : ")
			num1 = int(hex_str, 8)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in BIN : ",bin(num1))
			
			hex_str2 = input("\nPlease enter the base: ")
			num2 = int(hex_str2, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=math.log(num1,num2)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LN'):
			hex_str = input("Please enter the number : ")
			num1 = int(hex_str, 8)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in BIN : ",bin(num2))
			
			result=math.log(num1)
			print("\nthe result in DEC = ",result)
	
		else:
			print("Not valid operation")

	elif(type_number=='BIN'):
		if(operation=='ADD'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1+num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SUB'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1-num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='MUL'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1*num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='DIV'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1/num2
			print("\nthe result in DEC = ",result)
			
		elif(operation=='MODULS'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1%num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='AND'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1&num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='OR'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1|num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='XOR'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=num1^num2
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='POWER'):
			hex_str = input("Please enter the number : ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter the power number: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=pow(num1,num2)
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='NOT'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			result=~num1
			print("\nthe result in HEX = ",hex(result))
			print("the result in DEC = ",result)
			print("the result in OCT = ",oct(result))
			print("the result in BIN = ",bin(result))
			
		elif(operation=='SQRT'):
			hex_str = input("Please enter number : ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			result=math.sqrt(num1)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LOG'):
			hex_str = input("Please enter number 1: ")
			num1 = int(hex_str, 2)
			print("equivalent number1 in HEX : ",hex(num1))
			print("equivalent number1 in DEC : ",(num1))
			print("equivalent number1 in OCT : ",oct(num1))
			
			hex_str2 = input("\nPlease enter number 2: ")
			num2 = int(hex_str2, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=math.log(num1,num2)
			print("\nthe result in DEC = ",result)
			
		elif(operation=='LN'):
			hex_str = input("Please enter the number : ")
			num1 = int(hex_str, 2)
			print("equivalent number2 in HEX : ",hex(num2))
			print("equivalent number2 in DEC : ",(num2))
			print("equivalent number2 in OCT : ",oct(num2))
			
			result=math.log(num1)
			print("\nthe result in DEC = ",result)
	
		else:
			print("Not valid operation")

	else:
		print("Not valid type number")
		
	print("To exit from the calculator enter 0 and enter any another number to continue ")
	des = int(input(">"))
	if(des==0):
		break

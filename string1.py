while True:
	print("\n1.Concatination")
	print("2.Repetition")
	print("3.Reversing")
	print("4.Range Slicing")
	print("5.Slicing")
	print("6.Upper Case")
	print("7.legth of string")
	print("8.Comparision")
	print("9.Sorted")
	print("10. check for the character present or not\n")
	ch=int(input("Enter the choice"))
	if ch==1:
		str1=input("Enter the string1: ")
		str2=input("Enter string2: ")
		str3=str1+str2
		print("Concatination of str1 and str2 is: ",str3)
	elif ch==2:
		str1=input("Enter string: ")
		n=int(input("Enter the number of time to be repeat"))
		print("The string is: ",str1*n)
	elif ch==3:
		str1=input("Enter the string: ")
		print("Reverse order of the given string is: ",str1[::-1])
	elif ch==4:
		str1=input("Enter the string: ")
		n=int(input("Enter the starting range"))
		m=int(input("Enter the ending range"))
		print("The string is: ",str1[n:m])
	elif ch==5:
		str1=input("Enter the string")
		n=int(input("Enter the index value"))
		print("The index value is: ",str1[n])
	elif ch==6:
		str1=input("Enter the string")
		print("The upper case of given string is",str1.upper())
	elif ch==7:
		str1=input("Enter the string")
		print("Length of the given string is: ",len(str1))
	elif ch==8:
		str1=input("Enter the first string")
		str2=input("Enter the second string")
		print(str1==str2)
	elif ch==9:
		str1=input("Enter the string")
		print("The sorted string is",''.join(sorted(str1)))
	elif ch==10:
		str1=input("Enter the string")
		n=input("Enter the character for checking")
		print(n in str1)
	else:
		exit()


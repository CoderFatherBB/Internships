# Four Example of String

str1 = "This is First Example of String."
str2 = "This is Second Example of String."
str3 = "This is Thired Example of String."
str4 = "This is Fourth Example of String."

print(str1 + "\n" + str2 + "\n" + str3 + "\n" + str4 + "\n")



# Four Example of Lists and its Opreations
list1 = [1, 2, 3, 4]    ### This is a list of Integers 
list2 = [1.1, 2.2, 3.3, 4.4]    ### This is a list of Floats 
list3 = ["Hello", 'I', "am", "bhavin"]   ### This a list of char and string 
list4 = ["hello", 2, 4.4]   ### This is a example of lists with diffrent datatype 

print(list1,list2,list3,list4)
print(list1[1:3]) # Slicing of the list1
list2[2] = 5.5 # reassigning the value in list2 at index 2
print(list2)



print("\n")
# Four Example of Dictionary and its Opreations
Dict1 = {"Name" : "Bhavin", "Age" : 19, "Gender" : "Male"}
Dict2 = {int : 5, float : 2.2, True : 1, False : 0}
Dict3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
Dict4 = {'A' : 1, 'B' : 3, 'A' : 4, 'C' : 3}

print(Dict4) # it removes the duplicats and prints the latest value assign
print(Dict1["Name"]) # accessing the element in dictionary using key word
print(Dict3.get('d')) # accessing with get function
Dict2[float] = 5.5 # reassigining the value
print(Dict2)

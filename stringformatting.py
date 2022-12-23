#Strings in Python can be formatted with the use of format() method which is a very versatile and powerful tool for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order

#default method
string1 = "{} {} {} {}\n ".format("beast","incarnate","brock","lesnar")
print(" default method")
print(string1)

#position method
string2 = "{1} {3} {2} {0}\n ".format("let","your","dreams","blossom")
print("postion method")
print(string2)

#keyword formatting
string = "{l} {f} {g}\n".format("l = life","f = fuck","g = geek")
print("keyword formatting")
print(string)
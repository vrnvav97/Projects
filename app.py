# @author Varun Agrawal

# Basic Variables
test_string='This is a test string'
test_numeric=10

print("String Data Type ",test_string)
print("Numeric Data Type ",test_numeric)


# List Data Structure
print ("Printing list values")
my_first_list=[10,20,30,40,50]

for i in my_first_list:
    print(i)


# If else condition
print ("If else conditional block")
flag=False

if flag:
    print ("Flag Value is True")
else:
    print ("Flag Value is false")        

# If elif else condition
print ("If elif else conditional block")
num=10
if num>5:
    print ("Number if > 5")
elif num<5:
    print ("Number is < 5")
else:
    print ("Number is = 5")    


#While loop
print ("While Loop Condition")

num = 1
while num<=10:
    print("Value of num ", num)
    num+=1

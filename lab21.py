# Introduction to looping
# it will print from 0 to 3
for i in range(4):
    print(i)
# End function will print in same line , seperate by space

for i in range (10):
    print(i, end =" ")
# create list of bowl
fruits=["apple","pears", "grapes"]
print(fruits)
# now lets use for loop
for fruit in fruits:
    print(fruit)
#Lets try different way
foo =open("ourfile.txt","w")
for fruit in fruits:
    print(fruit, file=foo)
    foo.close()
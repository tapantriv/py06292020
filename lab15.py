#String Methods
trek= "ncc 1701-d"
a= "the prime directive"
#using split method

a= a.split()
print(a)
# using join method result will be the_prime_directive
a = "_".join(a)
print(a)
# create a small string
lilstring = "Alta3 Research offers classes on Python coding"
newlist= lilstring.split(" ")
print(newlist)
# create a list of strings
myiplist = ["192", "168", "0", "12"]
#use join mehtod here
mynewiplist= ".".join(myiplist)
print(mynewiplist)
# Example 1 Print statement + Variables 
print("Hello, Python!")
# Example on assigning variables 
myvar = 10
print(myvar)
type(myvar)

myvar = "raghava"
print(myvar)
type(myvar)

mynum = 13
myname = "raghava"
# throws an error
#print("My name: " + myname + ", my number: " + mynum)

# Now it works when we convert number into string
print("My name: " + myname + ", my number: " + str(mynum))


# variables and operators
x = 10
y = 5

# arithmetic operators on numerical values!
print(x * y)

print(x + y)

name = 'raghava'

# throw error as + is not overloaded between int and string
print(x + name)

# works fine if you convert int  into string
print(str(x) + name)

# throw error as / is not overloaded between int and string
print(name / 2)




# Note that * is overloaded between int and string
print (x * name)

z = x * name

print(z)
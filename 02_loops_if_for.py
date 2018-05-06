# Example 2 Loops
x = int(input("Please enter an integer: "))

if x < 50:
   print("Your number is less than 50.", x)
elif x> 50 and x < 100:
   print("Your number is in between 50 - 100.", x)
else:
   print("Your number is more than 100.", x)

# Initialization of lists 
words = ['cat', 'window', 546]

for w in words:
   print(w, len(str(w)))

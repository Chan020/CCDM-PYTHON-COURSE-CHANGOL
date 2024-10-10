Age = int(input("Enter your age: \n"))
#if statements
if Age>=12 and Age<=27:
    print("You are Gen Z")

elif Age>=28 and Age<=43:
    print("You are Millennial")

elif Age>=44 and Age<=59:
    print("Your are Gen X")

elif Age>=60 and Age<=78:
    print("You are Boomers")

else:
    print("Sorry! You are out of Bounds...")
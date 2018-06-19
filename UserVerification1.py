inputString = input("Enter a String ")
try:
    inputInt = int(input("Please enter an integer "))
    inputFloat = float(input("Provide a float "))
except ValueError:
    print("Make sure you read the instructions")
    exit(1)

if len(inputString) > 1 and isinstance(inputInt,int) and isinstance(inputFloat,float):
    print("Access Granted, Welcome Mr. Robot")

else:
    print("NO YOU FOOL!! The pattern is STRING INT FLOAT, remember that")

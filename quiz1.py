number1 = input("What is the first number you would like to pick?")
number2 = input("What is the second number you would like to pick?")

sum = int(number1) + int(number2)

prod = int(number1) * int(number2)

while (sum != prod):
    print("Really? You thought that would work? Try again .")
    number1 = input("First number?")
    number2 = input("Second number?")
    sum = int(number1) + int(number2)
    prod = int(number1) * int(number2)

print("You did it, the sum and product are equal... What exactly did you gain again?")
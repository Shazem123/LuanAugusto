def num_class(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


print("Welcome to the even/odd number classifier!")
while True:
    number = int(input("Select your number (0 to exit): "))

    if number == 0:
        print("Alright! Program finished.")
        break

    result = num_class(number)
    print(f"{number} is {result}.")

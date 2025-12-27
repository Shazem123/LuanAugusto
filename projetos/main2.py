age = int(input("Welcome to the age and role identification program! Please enter your age: "))

if age < 13:
    role = "Child"
elif age < 18:
    role = "Teenager"
elif age < 60:
    role = "Adult"
else:
    role = "Senior"

if role == "Child":
    print("Congratulations! You are classified as a Child. Enjoy your childhood!")

elif role == "Teenager":
    print("Great! You are classified as a Teenager. Embrace your teenage years!")

elif role == "Adult":
    print("You are classified as an Adult. Time to take on responsibilities!")

else:
    print("You are classified as a Senior. Enjoy the wisdom and experience you've gained!")
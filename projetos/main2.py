age = int(input("Welcome to the age and role identification program! Please enter your age: "))

while age < 0:
    age = int(input("Invalid age. Please enter a valid age: "))

if age < 13:
    role = "Child"
    message = "Enjoy your childhood!"
elif age < 18:
    role = "Teenager"
    message = "Take your time on your teenage years."
elif age < 60:
    role = "Adult"
    message = "You are in your prime. Grapple your responsibilites well."
else:
    role = "Senior"
    message = "You lived your life to its fullfilest and is now full of wisdom."

print(f"You are classified as a {role}. {message}")
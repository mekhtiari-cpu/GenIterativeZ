# ask for name
# ask for your birth year
# reply with Hello [name], I can see your are [age]
# use copilot to do this, and run code

name = input("Enter your name: ")
print("What's up " + name)
birthYear = input("What year were you born in? ")

if int(birthYear) > 2002:
    print("You were born in " + birthYear + "? Damn you're old!")
elif int(birthYear) == 2002:
    print("Are we secret twins? I was born in " + birthYear + " too!")
else:
    print("Awe tiny baby. I thought people born in " + birthYear + " didnt exist yet...")


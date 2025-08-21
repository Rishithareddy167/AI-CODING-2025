def group_age(age):
    if age < 13:
        print("child")
    elif age >= 13 and age <= 19:
        print("teen")
    elif age >= 20 and age <= 59:
        print("adult")
    else:
        print("senior citizen")

# Get input and call the function
age = int(input("Enter the age: "))
group_age(age)
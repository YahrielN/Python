def allowed_dating_age(my_age):
    girls_age = my_age//2 + 7
    return girls_age

s=1
while s == 1:
    name = input("Name:")
    age = int(input("Age:"))

    if age < 13:
        print ("You are too young to date.")
    elif age >13:
        age_limit = allowed_dating_age(age)
        print(name, "can date", age_limit, "year old or older.")

    s = int(input("Press 1 to continue or Press 0 stop:"))

    if s > 1:
        s = int(input("This value is invalid. \nPlease try again:"))





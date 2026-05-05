age = int(input("Enter your age -->"))

if age >= 18:
    # nested if_else condition
    test = input()
    if test == "PASS":
        print("Eligible for Driving License")
    else:
        print("Not Eligible for Driving License")
else:
    print("Not Eligible for Driving License")
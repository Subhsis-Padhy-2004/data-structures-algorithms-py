
age = int(input("Enter your age -->"))
if age >=80:
    print("S.senior")
elif age >=60 and age <=80:
    print("senior")
elif age >=25 and age <=60:
    print("genral")
elif age >=16 and age <=25:
    print("teen")
else:
    print("baby")
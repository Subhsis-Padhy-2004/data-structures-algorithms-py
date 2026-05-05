temp = int(input("Enter the current temp-->"))
if temp<=50 and temp>=25:
    print("Hot")
elif temp<=24 and temp >=10:
    print("cold")
elif temp<10:
    print("extremely Cold")

# Ternary Operator

age = int(input())

result = "Eligible" if age >= 18 else "Not Eligible"
print(result)

first = int(input("Enter first name"))
second = int(input("Enter second name"))
third = int(input("Enter third name"))

if first > second and first > third:
    print(first, "is the largest number")

elif second > first and second > third:
    print(second, "is the largest number")

else:
    print(third, "is the largest number")
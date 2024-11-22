try:
    num = int(input("Your number: "))

except ValueError:
    print("try again.")
    exit(1)

if num > 25:
    print("Error")
else:
    for i in range(num, 26):
        print(i)

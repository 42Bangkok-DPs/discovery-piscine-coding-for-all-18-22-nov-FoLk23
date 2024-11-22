def print_multiplication_table(num):
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

for num in range(1, 11):
    print_multiplication_table(num)

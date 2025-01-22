n = int(input("Enter the number: "))
sum = 0

for i in range(2, n + 1):  # Start from 2 as 1 is not a prime number
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        sum += i

print("The sum of prime numbers is:", sum)

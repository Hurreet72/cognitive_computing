def prime(n):
    sum = 0

    for i in range(2, n + 1):  # Start from 2 as 1 is not a prime number
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break  # Corrected the break statement

        if is_prime:
            sum += i

    return sum  # Return the sum of prime numbers

# Call the function and print the result
print("The sum is -->", prime(8))

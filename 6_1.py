def odd(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum += i
    return sum

print("The sum is:", odd(15))

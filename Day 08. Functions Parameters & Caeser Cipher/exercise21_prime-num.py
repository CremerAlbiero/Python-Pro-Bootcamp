def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print("It's not a prime number.")

# Do NOT change any of the code below
n = int(input("Insert a number: "))
prime_checker(number=n)
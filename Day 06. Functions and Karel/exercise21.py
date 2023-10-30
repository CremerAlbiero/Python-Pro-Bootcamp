# Define a function to check if a number is prime
def prime_checker(number):
    if number <= 1:
        print("Not prime")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not prime")
            return
    print("Prime")

n = int(input("Enter a number: "))
prime_checker(number=n)
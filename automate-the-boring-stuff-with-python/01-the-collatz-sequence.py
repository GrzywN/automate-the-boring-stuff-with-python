def collatz(number):
    output = 0

    if number % 2 == 0:
        output = number // 2
    else:
        output = 3 * number + 1

    print(output)
    return output
try:
    user_input = int(input("Pass the number: "))
    number = user_input
except ValueError:
    print("You must pass the number!")
    exit()

while True:
    number = collatz(number)
    if number == 1:
        break

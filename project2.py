print("Please enter a positive integer: ")
userNumber = int(input())

if userNumber > 1:
    for i in range(2, userNumber):
        if (userNumber % i) == 0:
            print(str(userNumber) + " is not a prime number")
            break
    else:
        print(str(userNumber) + " is a prime number")
else:
    print(str(userNumber) + " is not a prime number")
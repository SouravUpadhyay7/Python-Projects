import random


num = random.randrange(1000, 10000)

n = int(input("Guess the 4-digit number: "))


if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0  

   
    while n != num:
        ctr += 1
        count = 0

        n = str(n)
        num_str = str(num)  

       
        for i in range(4):
            if n[i] == num_str[i]:
                count += 1

        if count > 0:
            print(f"Not quite the number. But you did get {count} digit(s) correct!")
        else:
            print("None of the numbers in your input match.")

        print()
        n = int(input("Enter your next choice of numbers: "))

    
    ctr += 1
    print("You've become a Mastermind!")
    print(f"It took you only {ctr} tries.")

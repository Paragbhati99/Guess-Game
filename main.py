
'''We are going to write a program that generates a random number and asks the user to 
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number.
Hint: Use the random module'''


import random
n = random.randint(1,100)
a =int(input("Guess The Number: "))
a = -1
guesses = 0

while(a != n):
    guesses =1
    if(a > n):
        print("Lower Number Please: ")
        a = int(input("Guess The Number: "))
        guesses +=1
        
    elif(a < n):
        print("Higher Number Please: ")
        a = int(input("Guess The Number: "))
        guesses +=1
        
    else:
        print("You Guessed The Number: ")
        print(f"Number Of Guesses Used: {n} correctly in : {guesses} attempts")
         
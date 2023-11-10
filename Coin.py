# First we import the "Choice" function from the random module and the 
# reason why i didn't import the whole random library because it can 
# make a tiny bit of performance downgrade.
# You can import the whole library if you want.
from random import choice

# Now we create a function name head_or_tails (I couldn't think of any professional name)

def head_or_tails():

#   Now i created a variable coin which i assigned to a list which containes heads or tails
#   and then gave to the random.choice function which i later assigned to computer, the reason
#   why i used the .lower() function is because some people might write it in uppercase or lowercase
#   you can make it whatever case suits you

    coin = ['Heads', 'Tails']
    computer = random.choice(coin).lower()

#   After that i took the input from the user and lowercased it, Why you may ask its written ↑ 
#   then i printed computer so it can be sure that we know what came

    user = input("Heads or tails ? ").lower()
    print(computer)

#   Now, you might be able to tell what this code means, right.
#   No, well heres a brief explanation
#   We used an if statement to see if the the value the user chosed si equal to the value computer chose
#   If it is true we print you win if fase you lose

    if user == computer:
        print("You win!")
    else:
        print("You lose.")

#   Now the real code begins here
#   We use a while loop and give it a condition that do you want to play and took he users input and lowercased it
#   Now, if the you chose No you whould break the while loop and will not be able to play and brek out of the loop
#   But if you chose yes you will later on continue the loop and later be able to play

while True:
    print("Do you want to play?:")
    human = input("Yes or No : ").lower()

    if human == "no":
        print("bye bye")
        break
    elif human != "yes":
        print("Invalid Input")
        continue

    head_or_tails()

# Hope you like it

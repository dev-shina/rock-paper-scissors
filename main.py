import random   

options= ["R","P","S"]

def get_options(input):
    if input == "R":
        return "Rock"
    elif input == "P":
        return "Paper"
    elif input == "S":
        return "Scissors"

        
print("ROCK, PAPER, SCISSORS")
print("[R]=Rock, [P]=Paper, [S]=Scissors and [Q]=Quit")
Counter = 1

while True:
    print("Round " + str(Counter)+ ":")
    print("Enter a choice: ")
    user_option = input()

    if user_option == "Q":
        print("Thank you for playing!!")
        break

    random_index = random.randint(0,2)
    computer_option = options[random_index]
       
    print("You chose " + get_options(user_option)+ "\n" + "Computer chose" + get_options(computer_option))

    if user_option == "R" and computer_option == "S":
        print("You win, Rock beats Scissors")

    elif user_option == "P" and computer_option == "R":
        print("You win, Paper beats Rock")  

    elif user_option == "S" and computer_option == "P":
        print("You win, Scissors beats Paper")    

    elif user_option == "R" and computer_option == "P":
        print("Computer wins, Paper beats Rock")

    elif user_option == "P" and computer_option == "S":
        print("Computer wins, Scissors beats Paper")
    
    elif user_option == "S" and computer_option == "R":
        print("Computer wins, Rock beats Scissors")

    elif user_option == computer_option:
        print("It is a Tie!")

    else:
        print("Please enter a valid option")


    Counter = Counter + 1
    print("\n")

       
        
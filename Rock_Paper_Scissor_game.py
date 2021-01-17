import random

# print multiple lines
print("Winning Rules of Rock,Paper and scissor: \n" + "Rock vs Paper => Paper Wins \n"
        + "Rock vs Scissor => Rock wings \n" + "Paper vs Scissor => Scissor Wings")

# We have to use here while loop beacause here is many type of conditon
while True:
    print("Enter your choice: \n" + "1. Rock \n" + "2. Paper \n" + "3. Scissor")
    # take the input using integer
    choice = int(input("User Turn: "))
    # if any one currect then it shows true vlue
    while choice > 3 or choice < 1:
        choice = int(input("Invallid Input"))

    # Initialize value of choice which is processing here
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("User Input: ", choice_name)
    print("Now It's Computer Turn.................")

    # Computer Turn ramdomly number
    comp_choice = random.randint(1,3)

    # Looping util comp_choice 
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    # Initialize the value of comp_choice name
    if comp_choice == 1:
        comp_choice = 'Rock'
    elif comp_choice == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissor'

    print("Computer choice: ", comp_choice)
    print(choice_name + " vs " + comp_choice)

    # Main condition for winning
    if((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock Wins ==>", end = "")
        result = "Rock"
    elif((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print("Paper Wins ==>", end = "")
        result = "Paper"
    else: 
        print("Scissor Wins ==>", end = "")
        result = "Scissor"

    # print aither User or computer wins than print 
    if(result == choice_name):
        print("*******************USER WINS***************")
    else:
        print("******************COMPUTER WINS****************")

    print("Do you want to play again(y/N): ")
    ans = input()
    if (ans == "n" or ans == "N"):
        break

print("\n ...Thanks for playing...")    


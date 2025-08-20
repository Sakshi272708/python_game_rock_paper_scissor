print("welcome to the game")
list=["rock","paper","scissor"]
user=input("ur turn")
import random
system=random.choice(list)
print(system)
if (user==system):
    print("both chooses same draw means :- Tie")
elif user == "rock":
    if(system =="paper"):
        print("paper cover rock = system win")
    else:
        print(" rock smashes scissor = user win")
elif user == "paper":
    if(system =="rock"):
        print("paper covers rock = user win")
    else:
        print("scissor cuts paper = system win")
elif user == "scissor":
    if(system == "rock"):
        print("rock smashes scissor = system win")
    else:
        print("scissor cuts paper= user win")
# import random
# item_list = ["Rock", "Paper", "Scissor"]

# user_choice = input("Enter your move = Rock, Paper, Scissor= ")
# comp_choice = random.choice(item_list)

# print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

# if user_choice == comp_choice:
#     print("Both chooses same: = Match Tie")

# elif user_choice == "Rock":
#     if comp_choice == "Paper":
#         print("Paper covers Rock = Computer Win")
#     else:
#         print("Rock smashes Scissor = You win")

# elif user_choice == "Paper":
#     if comp_choice == "Scissor":
#         print("Scissor cuts paper, Computer Win")
#     else:
#         print("Paper covers rock, You win")

# elif user_choice == "Scissor":
#     if comp_choice == "Paper":
#         print("Scissor cuts paper, You win")
#     else:
#         print("Rock smashes scissor, Computer win")  


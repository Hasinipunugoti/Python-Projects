import random
rock='✊'
paper='✋'
scissors='✌️'
images_list=[rock,paper,scissors]
user_choice=int(input("Enter your choice(0 for rock, 1 for paper, 2 for scissors)=  "))
if user_choice>=3 or user_choice<0:
    print("You have entered invalid input. You lose")
else:
    print(f"User_choice= {images_list[user_choice]}")
    computer_choice=random.randint(0,2)
    print(f"Computer_choice= {images_list[computer_choice]}")
    if user_choice==computer_choice:
        print("Play again")
    elif user_choice==0 and computer_choice==2:
        print("You won")
    elif user_choice==2 and computer_choice==0:
        print("You lose")
    elif computer_choice>user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You won")
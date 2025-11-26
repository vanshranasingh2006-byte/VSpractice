# rock paper sicssor 
import random 
def game():
    choice_game=['rock','paper','sicssor']
    while True:     
        user_input=input("Please enter rock , sicssor or paper or enter q/Q to quit : ").lower().strip()
        if user_input=='q':
            print("thx for playing")
            break
        if user_input not in choice_game:
            print("invalid input")
            continue
        comp=['rock','paper','sicssor']
        computer_choice=random.choice(comp)
        print(f"the computer choice is {computer_choice}")
        if computer_choice==user_input:
            print("its a tie")
        elif (user_input=='rock' and computer_choice=='sicssor') or (user_input=='paper' and computer_choice=='rock') or (user_input=='sicssor' and computer_choice=='paper'):
            print(f"{user_input} beats {computer_choice} , hence u win , congratulation \n")
        else:
            print("ohh no try once again\n")

game()
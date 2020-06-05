# ✊🏻 ✋🏻 ✌🏻 🧔 💻 🎉 💀 🏆 ⛔ 🗑

import random

player_trophy = 0
computer_trophy =0
print("✊🏻=0 ✋🏻=1 ✌🏻=2")

while player_trophy < 3 and computer_trophy < 3 :
    player_input = int(input("🧔: "))
    if player_input == 0:
        player_input ="✊🏻"
    elif player_input==1:
        player_input="✋🏻"
    elif player_input==2:
        player_input="✌🏻"
    else:
        print("Error ⛔")
        print("")
        continue
    print("🧔:"  + player_input)
    computer_input=random.randrange(3)

  

    if computer_input == 0:
        computer_input ="✊🏻"
    elif computer_input==1:
        computer_input="✋🏻"
    else:
        computer_input="✌🏻"
    
    print("💻: " + computer_input)


    #logics
    if player_input==computer_input :
        print("Darw 🗑")
        
    elif player_input=="✊🏻":
        if computer_input=="✋🏻":
            computer_trophy+=1
            print("You Lose 💀")
        else:
            player_trophy+=1
            print("You Won 🎉")
    
    elif player_input == "✌🏻":
        if computer_input == "✊🏻":
            computer_trophy += 1
            print("You Lose 💀")
        else:
            player_trophy += 1
            print("You Won 🎉")
    
    elif player_input == "✋🏻":
        if computer_input == "✌🏻":
            computer_trophy += 1
            print("You Lose 💀")
        else:
            player_trophy += 1
            print("You Won 🎉")
        

    print(player_trophy * "🏆" + " vs. " + computer_trophy * "🏆")
    if player_trophy==3:
        print("Congrulation 🎉🎉🎉")
    elif computer_trophy==3:
        print("Defeated 💀💀💀")
    print("")

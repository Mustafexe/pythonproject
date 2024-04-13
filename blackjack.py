import random
again_and_again=False
while not again_and_again:
    your_cards = [random.randint(1, 11), random.randint(1, 10)]
    computer_first_card = random.randint(1, 11)
    print(f"Your cards = {your_cards}")
    print(f"Computer first card = {computer_first_card}")
    computer_cards = []
    check_point = False
    toplam = int()
    toplam2 = int()
    computer_cards.append(computer_first_card)
    computer_finals_hand = []

    while not check_point:
        check = input("Type 'Y' to get another card,type 'N' to pass").lower()
        if check == "y":
            new_card = random.randint(1, 10)
            your_cards.append(new_card)

            toplam = 0
            for number in your_cards:
                value = int(number)
                toplam = toplam + value
            print(f"your cards = {your_cards} and your curent score = {toplam}")
            if toplam > 21:
                check_point = True
                print("You lose")
        else:
            check_point = True
            toplam = 0
            for number in your_cards:
                value = int(number)
                toplam = toplam + value
            print(f"your cards = {your_cards} and your curent score = {toplam}")

    if toplam > 21:
        print(":(")
    else:
        while toplam2 < 17:
            toplam2 = 0
            computer_cards.append(random.randint(1, 11))
            computer_finals_hand = computer_cards
            for number in computer_cards:
                value = int(number)
                toplam2 = toplam2 + value
                if toplam2 > 21:
                    print(f"You win computer's hand = {computer_finals_hand} and score = {toplam2}")
        if toplam < 22 and toplam > toplam2:
            print(f"Computer's hand = {computer_finals_hand} and score ={toplam2}")
            print("You win")
        elif toplam < 22 and toplam == toplam2:
            print(f"Computer's hand = {computer_finals_hand} and score ={toplam2}")
            print("Draw")
        elif toplam < toplam2 and toplam2 < 22:
            print(f"Computer's hand = {computer_finals_hand} and score ={toplam2}")
            print("You lose")
    check2=input("Do you want to play game of BlackJack 'Y' or 'N' ").lower()
    if check2=="n":
        again_and_again=True
        print("See you later")
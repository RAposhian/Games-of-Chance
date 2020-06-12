import random

money = 100

#Write your game of chance functions here

def coin_flip():
  user_call = ''
  user_call = input("Call heads or tails: \n")

  coin_side = ''
  coin = random.random()
  coin = round(coin)
  
  if coin == 0:
    coin_side = 'heads'
  elif coin == 1:
    coin_side = 'tails'
    

  if user_call == coin_side:
    print("You have guessed correctly! The flip was " + coin_side + '!')
    return True
  elif user_call != coin_side:
    print("You have guessed incorrectly! The flip was " + coin_side + '!')
    return False


def cho_han():
    user_call = ''
    user_call = input("Call if the dice roll adds up to an even number or a odd number: \n").lower()

    dice_roll_one = random.randint(1, 6)
    dice_roll_two = random.randint(1, 6)

    dice_sum = dice_roll_one + dice_roll_two

    even_odd = ''
    if dice_sum % 2 == 0:
        even_odd = 'even'
    else: 
        even_odd = 'odd'
    
    if user_call == even_odd:
        print('You are correct! The roll was: ' + even_odd + '!')
        return True
    else:
        print('You are incorrect! The roll was: ' + even_odd + '!')
        return False

def high_card():
    user_one_card = random.randint(1, 13)
    user_two_card = random.randint(1, 13)


    if user_one_card > user_two_card:
        print('You have won with: ' + str(user_one_card) + ' against: ' + str(user_two_card))
        return True
    elif user_two_card > user_one_card:
        print('You have lost with: ' + str(user_one_card) + ' against: ' + str(user_two_card))
        return False
    elif user_one_card == user_two_card:
        print('You have tied! The game will restart.')
        return high_card()
        

    


choice = input("""What game do you want to play?
===================
Coin Flip
Cho-Han
High Card
""").lower()
bet = int(input("How much do you want to bet?\n"))

if choice == "coin flip":
    result = coin_flip()
    if result:
        money += bet
    else:
        money -= bet
elif choice == 'cho-han':
    res = cho_han()
    if res:
        money += bet
    else:
        money -= bet
elif choice == 'high card':
    result = high_card()
    if result:
        money += bet
    else:
        money -= bet

    



print("You now have $" + str(money))



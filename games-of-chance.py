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

    

choice = input("""What game do you want to play?
===================
Coin Flip
""")
bet = int(input("How much do you want to bet?\n"))

if choice == "Coin Flip":
    result = coin_flip()
    if result:
        money += bet
    else:
        money -= bet

#Call your game of chance functions here
print(money)



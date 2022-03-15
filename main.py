import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.🤨")

answer = random.randint(1,100)
#print(answer)

level = input("Choose a level 'easy' or 'hard': ")

if level == 'easy':
  attempt_num = 10
elif level == 'hard':
  attempt_num = 5
else:
  print("Error level is not defined.")
  attempt_num = 0
is_game_over = False

while is_game_over == False:
  print(f"You have {attempt_num} attempts remaining to guess the number.")
  guess = int(input("❓Make a guess: "))
  if attempt_num == 0:
    print("You don't have any attempts to guess. Game over.❌ ")
    print(f"The answer was {answer}")
    is_game_over = True
  else:
      if guess < answer:
        print("Too low.\nGuess again.")
        attempt_num = attempt_num - 1
      elif guess > answer:
        print("Too high.\nGuess again.")
        attempt_num = attempt_num - 1
      elif answer == guess:
        print(f"You guessed it right! The answer was {answer}. Congrats ☺️")
        is_game_over = True
  


  

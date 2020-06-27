
import random

name = input("What is your name? ")

max_guesses = input("How many guesses do you want to be given? ")
max_guesses = int(max_guesses)

num_guesses = 0;
number = random.randint(1,100)

print(f"{name}, I am thinking of a number between 1 and 100.")

while num_guesses < max_guesses:
  guess = input("Make your guess: ")
  guess = int(guess)
  num_guesses+=1

  guesses_left = max_guesses - num_guesses
  if guess < number:
    print(f"Your guess is too low! You have {guesses_left} guesses left.")

  elif guess>number:
    print(f"Your guess is too high! You have {guesses_left} guesses left.")

  else:
    break

if guess == number:
  print(f"Congrats! You guessed the number in {num_guesses} tries.")
if guess != number:
  print(f"You ran out of guesses! The number was {number}")
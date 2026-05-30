continents = ["Asia", "Africa", "North America", "South America", "Antarctica",
"Europe", "Australia"]
guessed = []
attempts = 0
# determines if user's guess is one of the continents
def isContinent(guess):
  # checks if guess was already made
  if guess in guessed:
    return "guessed"
  for continent in continents:
    # goes through list of continents until user's guess is equal to continent
    if guess == continent:
      return "correct"
  # if guess isn't equivalent to any of the items
  return "incorrect"
# user keeps guessing until all 7 continents guessed
while len(guessed) < 7:
  remaining = 7 - len(guessed)
  user_guess = input(f"Enter a continent ({remaining}/7 remaining):
").strip().title()
  result = isContinent(user_guess)
  attempts += 1
  # show user result of guess
  if result == "correct":
    guessed.append(user_guess)
    print(f"Correct! {user_guess} is a continent.")
  elif result == "incorrect":
    print(f"Incorrect! {user_guess} is not a continent.")
  else:
    print(f"You already guessed {user_guess}.")
print(f"You named all 7 continents in {attempts} attempts!")

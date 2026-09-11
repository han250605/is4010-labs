import random


def generate_mad_lib(adjective, noun, verb):
	"""Return a nonempty story containing all three supplied words."""
	return f"The {adjective} {noun} decided to {verb} through the park."


def guessing_game():
	"""Run an interactive number-guessing game."""
	secret_number = random.randint(1, 100)

	while True:
		guess = int(input("Guess the number: "))

		if guess < secret_number:
			print("Too low.")
		elif guess > secret_number:
			print("Too high.")
		else:
			print("Correct!")
			break

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

base_url = "http://quotes.toscrape.com/"

def read_quotes(filename):
	with open(filename, 'r',encoding="utf-8") as file:
		csv_reader = DictReader(file)
		quotes = list(csv_reader)
		return quotes

def start_game(quotes):
	quote = choice(quotes)
	num_guesses = 4
	print("Here\'s a Quote:")
	print(quote['text'])
	#print(quote['author'])
	guess = ''
	while guess.lower() != quote['author'].lower() and num_guesses > 0:
		guess = input(f'Who\'s the author of the quote? guesses remaining: {num_guesses}\n')
		if guess.lower() == quote['author'].lower():
			print('You Got it Right')
			break
		num_guesses -= 1
		if num_guesses == 3:
			res = requests.get(f"{base_url}{quote['link']}")
			soup = BeautifulSoup(res.text, 'html.parser')
			bday = soup.find(class_='author-born-date').get_text()
			birth_place = soup.find(class_='author-born-location').get_text()
			print(f"Here\'s the Hint: The author was born on {bday} {birth_place}")
		elif num_guesses == 2:
			print(f"Here\'s the Hint: The author\'s first name starts with: {quote['author'][0]}")
		elif num_guesses == 1:
			last_initial = quote['author'].split(" ")[1][0]
			print(f"Here\'s the Hint: The author\'s last name starts with: {last_initial}")
		else:
			print(f"Sorry ran out of guesses. The answer is {quote['author']}")

	again = ''
	while again.lower() not in ('y','n','yes','no'):
		again = input('Would you like to play again (y/n)?')
	if again.lower() in ('yes', 'y'):
		print('Okay! you play again')
		return start_game(quotes)
	else:
		print('GoodBye!!!')

quotes = read_quotes('quotes.csv')	
start_game(quotes)				
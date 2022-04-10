import os
import random
import nextcord
from nextcord.ext import commands
from replit import clear

PREFIX = "+"
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, help_command=None, status=nextcord.Status.idle, activity=nextcord.Streaming(name=f"testing wordle", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"), intents=intents)

channel_id = 962599139684782092 # channel id
grey_letters = {
	"a": "<:greya:956086083249131581>",
	"b": "<:greyb:956086344902393896>",
	"c": "<:greyc:956086384718929922>",
	"d": "<:greyd:956086412334215179>",
	"e": "<:greye:956086440373157919>",
	"f": "<:greyf:956086472652509194>",
	"g": "<:greyg:956086674994130974>",
	"h": "<:greyh:956086718543585292>",
	"i": "<:greyi:956086741897457675>",
	"j": "<:greyj:956086762940293150>",
	"k": "<:greyk:956086892623978559>",
	"l": "<:greyl:956086974261895188>",
	"m": "<:greym:956087001394855976>",
	"n": "<:greyn:956087020449562675>",
	"o": "<:greyo:956087040825495572>",
	"p": "<:greyp:956087062199668797>",
	"q": "<:greyq:956087081971613727>",
	"r": "<:greyr:956087102871863326>",
	"s": "<:greys:956087125709819954>",
	"t": "<:greyt:956087146916225054>",
	"u": "<:greyu:956087165530550313>",
	"v": "<:greyv:956087184031612938>",
	"w": "<:greyw:956087205753933854>",
	"x": "<:greyx:956087229825028136>",
	"y": "<:greyy:956087254743392317>",
	"z": "<:greyz:956087273877815296>",
}
green_letters = {
	"a": "<:greena:956087521907970068>",
	"b": "<:greenb:956087545496748032>",
	"c": "<:greenc:956087564450795520>",
	"d": "<:greend:956087586902904843>",
	"e": "<:greene:956087606725193838>",
	"f": "<:greenf:956087624731332648>",
	"g": "<:greeng:956087646386528256>",
	"h": "<:greenh:956087664359125023>",
	"i": "<:greeni:956087701369667664>",
	"j": "<:greenj:956087732722077736>",
	"k": "<:greenk:956087753492287518>",
	"l": "<:greenl:956087777441775616>",
	"m": "<:greenm:956087798161621003>",
	"n": "<:greenn:956087817002422302>",
	"o": "<:greeno:956087835671281664>",
	"p": "<:greenp:956087857242587167>",
	"q": "<:greenq:956087876771250186>",
	"r": "<:greenr:956087898606809159>",
	"s": "<:greens:956087918823354378>",
	"t": "<:greent:956087938322685962>",
	"u": "<:greenu:956087956282699777>",
	"v": "<:greenv:956087976063025184>",
	"w": "<:greenw:956087997638541342>",
	"x": "<:greenx:956088041364127745>",
	"y": "<:greeny:956088065057767424>",
	"z": "<:greenz:956088087556022342>",
}
yellow_letters = {
	"a": "<:yellowa:956088230921510952>",
	"b": "<:yellowb:956088258629079050>",
	"c": "<:yellowc:956088276920442920>",
	"d": "<:yellowd:956088328732688385>",
	"e": "<:yellowe:956088348064247848>",
	"f": "<:yellowf:956088368167526400>",
	"g": "<:yellowg:956088383178960896>",
	"h": "<:yellowh:956088400107147275>",
	"i": "<:yellowi:956088421590372392>",
	"j": "<:yellowj:956088442037620756>",
	"k": "<:yellowk:956088459028738078>",
	"l": "<:yellowl:956088476414144572>",
	"m": "<:yellowm:956088523545518151>",
	"n": "<:yellown:956088545410449428>",
	"o": "<:yellowo:956088562070224948>",
	"p": "<:yellowp:956088580193812490>",
	"q": "<:yellowq:956088603019182091>",
	"r": "<:yellowr:956088645381652520>",
	"s": "<:yellows:956088663563993098>",
	"t": "<:yellowt:956088684048941066>",
	"u": "<:yellowu:956088710397587498>",
	"v": "<:yellowv:956088728412106773>",
	"w": "<:yelloww:956088747651379230>",
	"x": "<:yellowx:956088797366460457>",
	"y": "<:yellowy:956088822117064754>",
	"z": "<:yellowz:956088843457691658>",
}

popular_words = open("words.txt").read().splitlines()
all_words = set(word.strip() for word in open("every_word.txt"))

word = random.choice(popular_words)
guess_count = 0
is_guess_word = False
is_on = True
wordle_guess_dict = {}

guessed = False


def is_valid_word(word):
	return word.lower() in all_words
	
def check_word(word, guess):
	global guessed
	index = 0
	word_output = []
	console_output = []
	if guess.lower() == word:
		guessed = True
		return "guessed"
		
	for char in guess.lower():
		if word[index] == guess.lower()[index]:
			letter = green_letters[char]
			console_letter = "🟩"
		elif guess[index].lower() in word and word[index] != guess.lower()[index]:
			letter = yellow_letters[char]
			console_letter = "🟨"
		else:
			letter = grey_letters[char]
			console_letter = "⬜"
		word_output.append(letter)
		console_output.append(console_letter)
	
		index += 1

		guessed = False
		
	return word_output, console_output, guessed

# print(f"hey the word is: {word} btw")

@bot.event
async def on_ready():
	global guess_count
	global is_on
	global wordle_guess_dict
    
	while guess_count < 6 and is_on:
		guess = input("Guess a word: ").lower()
		clear()
		if is_valid_word(guess):
			if is_guess_word == False:
				print(f" {guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}")
				answer_str = ""
				console_str = ""
				answer = check_word(word,guess)[0]
				for i in answer:
					answer_str += i
				await bot.get_channel(channel_id).send(answer_str)
				console_answer = check_word(word, guess)[1]
				wordle_guess_dict[guess_count] = console_answer
				
				for guess_number in wordle_guess_dict.keys():  # looping over each guess
					for l in wordle_guess_dict[guess_number]:  # looping over each letter in a guess
						console_str += l
					console_str += "\n"
				print(console_str)

				guess_count += 1  # adding to guess count
				if guessed:  # checking if guessed
					is_on = False
					print(f"the word was {word}! you guessed the word in {guess_count} guesses!")
		elif not is_valid_word(guess): # checking if guess is a valid word
			print("hey! the guess isnt valid")
	
		print(f"guess count: {guess_count}") # print the guess count


bot.run(os.environ['DISCORD_TOKEN'])

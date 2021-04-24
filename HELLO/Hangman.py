import random

stages = ['''+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['apple', 'mango', 'orange']

#choose a random word from the word_list
chosen_word = random.choice(word_list)

#print the chosen_word
print(chosen_word)

lives = 6
#display a blank list and count the number of word in the list
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += '_'

#with the false the loop will continue
end_of_game = False
while not end_of_game:
    guess = input('Guess a word: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')

    print(display)
    if '_' not in display:
        end_of_game = True
        print('you win')

#print the stages and number of lives
    print(stages[lives])
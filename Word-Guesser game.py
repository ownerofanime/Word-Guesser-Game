#this is the data bank for the random words
import random
wordbank = ['Hello', 'World', 'Python', 'Programming', 'Code', 'Random', 'Word', 'Game']
#picks out a random index number from the bank
keyword = int(random.randint(0, len(wordbank) - 1))
#puts that index number with the wordbank so that 
word_guess = wordbank[keyword].lower()
new_word = (len(word_guess))
underscore = "_" * new_word
#number of attempts that has been given.
attempts = 10 
#starting of the loop
while attempts > 0:
    print('\ncurrent word ' + ''.join(underscore))
    guess = input('Guess a letter: ').lower()
    if guess in word_guess:
      for x in range(len(word_guess)):
        if guess[x] == guess:
          word_guess[x] = guess
      print('Great guess!')
    else:
      print('oops! You seem to have guessed the wrong alphabet, try again!')
      attempts -= 1

#finding out the number of attempts
if '_' in word_guess:
  print('Oops! you have ran out of tries!')
else:
  print('congratulations! You have guessed all the words correctly!')
  
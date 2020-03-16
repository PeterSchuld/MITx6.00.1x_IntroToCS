# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return(False)
        
    return (True)
        
    # Function call: isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])  
    # correct output : False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    answer=""
    for char in secretWord:
        if char in lettersGuessed:
            answer+=char
        else:
            answer+= "_"
    
    return(answer)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    zeichenListe=list(string.ascii_lowercase)
    antwort = ''
    
    for letter in lettersGuessed:
        if letter in zeichenListe:
            zeichenListe.remove(letter)
            
    for char in zeichenListe:
        antwort += char
            
    return(antwort)        
            
        


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    import string
    initialString = string.ascii_lowercase
    print ('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord))+' letters long.')
    getLetter=''
    num=8
    guessedLetters =''
    
    while num > 0:
        print('-------------')
        if isWordGuessed (secretWord, getLetter):
            print('Congratulations, you won!')
            break
        print('You have '+str(num) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(getLetter))
        
        buchstabe = input('Please guess a letter: ')
        k_buchstabe = buchstabe.lower()
        
        getLetter +=k_buchstabe
        outString = getGuessedWord(secretWord, getLetter)
        
        # if the letters are guessed
        if k_buchstabe in secretWord:
            if k_buchstabe in guessedLetters: # output to remind repeat input
                print("Oops! You've already guessed that letter: " +outString)
            else:
                print('Good guess: '+ outString) # keep the num is not changed
                
        else:
            if k_buchstabe in guessedLetters:
                print("Oops! You've already guessed that letter: " + outString)
            else:
                print("Oops! That letter is not in my word: " + outString)
                num -=1
                
        guessedLetters +=k_buchstabe
        
    if num == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
        

secretWord = chooseWord(wordlist).lower()

# hangman ('senselessness') # test
hangman(secretWord)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)




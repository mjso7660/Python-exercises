# Problem Set 2, hangman.py
# Name: Min Joon So
# Collaborators: None
# Time spent: 2hrs

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    found = True
    if len(secret_word)==0 or len(letters_guessed)==0:
        return False
    for x in secret_word:
        found = False
        for y in letters_guessed:
            if x==y:
                found = True
                break
        if not found:
            return False
            break            
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    returnVal=""
    for x in secret_word:
        found = False
        for y in letters_guessed:
            if x==y:
                found = True
                returnVal += x
                break
        if found == False:
            returnVal +="_ "
    return returnVal
        



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    returnVal=""
    found=False
    for x in string.ascii_lowercase:
        found=False
        for y in letters_guessed:
            if x==y:
                found=True
                break
        if not found:
            returnVal+=x
    return returnVal
            
def count_unique(secret_word):
    '''
    secret_word: secret word we are guessing
    returns: integer, how many unique letters there are        
    '''
    compressed=""
    for x in secret_word:
        if not is_word_guessed(x,compressed):
            compressed+=x
    return len(compressed)
        
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed=""
    guesses_remaining=6
    warnings_remaining=3
    word_length=len(secret_word)
    
    print(word_length,"letters long")
    print(warnings_remaining,"warnings left")
    
    while (guesses_remaining!=-1) and (warnings_remaining!=-1) and not (is_word_guessed(secret_word,letters_guessed)):
        print("----------------------")
        print(guesses_remaining,"guesses left")
        print("available",get_available_letters(letters_guessed))
        guess=str(input("Please guess"))
        #weird letter
        if not str.isalpha(guess):
            warnings_remaining-=1
            print("Invalid letter. Remaining warnings: ",warnings_remaining)
            continue
        #guessed again
        elif is_word_guessed(guess,letters_guessed):
            print(guess, "/",letters_guessed)
            warnings_remaining-=1
            print("You've already guessed that one. Remaining warnings: ",warnings_remaining)
            continue
        #guessed something appropriate
        else:
            letters_guessed+=guess
            #right guess
            if is_word_guessed(guess, secret_word):
                print("Good guess",get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word,letters_guessed):
                    points=guesses_remaining*count_unique(secret_word)
                    print("Congratualations! Your score is",points)
                    return
            #wrong guess
            else:
                print("Not in my word: ", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(guess,'aeiou'):
                    guesses_remaining-=2
                else:
                    guesses_remaining-=1
                if guesses_remaining < 0:
                    print("You Lost")
                    return
                    
            
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    stripped=my_word.replace(" ","")
    #check length first
    if not len(stripped)==len(other_word):
        return False
    
    for x in range(len(stripped)):
        if stripped[x]=="_":
            if is_word_guessed(other_word[x],stripped):
                return False
            continue
        if not stripped[x]==other_word[x]:
            return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word=my_word.replace(" ","")
    list=""
    for x in wordlist:
        if len(x)==len(my_word) and match_with_gaps(my_word,x):
            list+=x+" "
    if list=="":
        print("no match found")
        return
    return list



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed=""
    guesses_remaining=6
    warnings_remaining=3
    word_length=len(secret_word)
    
    print(word_length,"letters long")
    print(warnings_remaining,"warnings left")
    
    while (guesses_remaining!=-1) and (warnings_remaining!=-1) and not (is_word_guessed(secret_word,letters_guessed)):
        print("----------------------")
        print(guesses_remaining,"guesses left")
        print("available",get_available_letters(letters_guessed))
        guess=str(input("Please guess"))
        if guess=="*":
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            continue
        #weird letter
        if not str.isalpha(guess):
            warnings_remaining-=1
            print("Invalid letter. Remaining warnings: ",warnings_remaining)
            continue
        #guessed again
        elif is_word_guessed(guess,letters_guessed):
            print(guess, "/",letters_guessed)
            warnings_remaining-=1
            print("You've already guessed that one. Remaining warnings: ",warnings_remaining)
            continue
        #guessed something appropriate
        else:
            letters_guessed+=guess
            #right guess
            if is_word_guessed(guess, secret_word):
                print("Good guess",get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word,letters_guessed):
                    points=guesses_remaining*count_unique(secret_word)
                    print("Congratualations! Your score is",points)
                    return
            #wrong guess
            else:
                print("Not in my word: ", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(guess,'aeiou'):
                    guesses_remaining-=2
                else:
                    guesses_remaining-=1
                if guesses_remaining < 0:
                    print("You Lost")
                    return



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

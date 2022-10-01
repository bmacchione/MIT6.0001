# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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
    secret_word_list=[]
    lg=[]
    for char in letters_guessed:
        lg.append(char)
    for char in secret_word:
        secret_word_list.append(char)
        if char in lg:
            secret_word_list.remove(char)
    return secret_word_list==[]



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess =[]
    positionlist=[]
    wordlist=[]
    for char in secret_word:
        guess.append("_")
        wordlist.append(char)
    for char in letters_guessed:
        if char in wordlist:
            for i in range(0, len(wordlist)):
                if char == wordlist[i]:
                    position = i
                    if position not in positionlist:
                        positionlist.append(position)
                        guess[position] = char
    guess_string=""
    for i in range(0, len(guess)):
        if guess[i]=="_":
            guess_string+=guess[i]+" "
        else:
            guess_string+=guess[i]
    return(guess_string)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alpha = string.ascii_lowercase
    alpha_list=[]
    alpha_result=""
    for char in alpha:
        alpha_list.append(char)
    for char in letters_guessed:
        alpha_list.remove(char)
    for i in range(0, len(alpha_list)):
        alpha_result+=alpha_list[i]
    return(alpha_result)
    
        
    
    

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
    
    num_guesses=6
    num_warnings=3
    letters_guessed=[]
    vowels=["a","e","i","o","u"]
    guessed = False
    sw_list=[]
    for char in secret_word:
        sw_list.append(char)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word with ",(len(secret_word))," letters long.")
    print("------------------")
    while num_guesses > 0:
        print("You have ",num_warnings," warnings left.")
        print("You have ",num_guesses," guesses left.")
        availabe_letters=get_available_letters(letters_guessed)
        print(availabe_letters)
        guess_letter=input("Please guess a letter: ")
        if guess_letter.isalpha():
            gl=guess_letter.lower()
            guess_letter=gl
            if guess_letter in letters_guessed:
                num_warnings = num_warnings-1
                if num_warnings <= 0:
                    num_guesses = num_guesses-1
                    num_warnings == 0
                print("Oops! You already guessed that letter.")
                print("-----------------")
            else:
                letters_guessed.append(guess_letter)
                current_guess=get_guessed_word(secret_word, letters_guessed)
                if guess_letter in sw_list:
                    print("Good guess: ",current_guess)
                    print("-------------------")
                    a=letters_guessed
                    guessed = is_word_guessed(secret_word, a)
                    if guessed == True:
                        break
                else:
                    print("Oops! That letter is not in my word: ",current_guess)
                    print("--------------------------")
                    if guess_letter in vowels:
                        num_guesses=num_guesses-2
                    else:
                        num_guesses=num_guesses-1      
        else:
            num_warnings = num_warnings-1
            if num_warnings <= 0:
                num_guesses = num_guesses-1
                num_warnings == 0
            print("Oops! That is not a valid letter.")
    if guessed == True:
        print("Congratulations, you won!")
        char_score=0
        char_list= []
        for char in secret_word:
            if char not in char_list:
                char_score +=1
                char_list.append(char)
        score = char_score*num_guesses
        print("Your total score for this game is: ",score)
    else:
        print("Sorry, you ran out of guesses.")
        print("The word is",secret_word)


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
    my_word_ls=[]
    other_word_ls=[]
    ow_nospace = other_word.strip()
    abc = string.ascii_lowercase
    abc_list = []
    values = []
    for char in abc:
        abc_list.append(char)
    for char in my_word:
        if char != " ":
            my_word_ls.append(char)
    for char in my_word_ls:
        if char != "_":
            abc_list.remove(char)
    for char in ow_nospace:
        other_word_ls.append(char)
    if len(my_word_ls) == len(other_word_ls):
        for i in range(0, len(my_word_ls)):
            if my_word_ls[i]==other_word_ls[i]:
                values.append(True)
            elif my_word_ls[i]=="_":
                if other_word_ls[i] in abc_list:
                    values.append(True)
                else:
                    return(False)
                    break
            else:
                return(False)
                break
        if len(values) == len(other_word_ls):
            return(True)
    else:
        return(False)
    



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
    my_word_ls=[]
    abc = string.ascii_lowercase
    word_ls=[]
    for char in my_word:
        if char != " ":
            my_word_ls.append(char)
    for word in wordlist:
        if len(word) == len(my_word_ls):
            other_ls =[]
            abc_list=[]
            values=[]
            for char in abc:
                abc_list.append(char)
            for char in my_word_ls:
                if char != "_":
                    if char in abc_list:
                        abc_list.remove(char)
            for char in word:
                other_ls.append(char)
            for i in range(0, len(my_word_ls)):
                if my_word_ls[i]==other_ls[i]:
                    values.append(True)
                elif my_word_ls[i]=="_":
                    if other_ls[i] in abc_list:
                        values.append(True)
                    else:
                        break
                else:
                    break
            if len(values) == len(my_word_ls):
                word_ls.append(word)
    if word_ls==[]:
        print("No matches found")
    else:
        print(word_ls)
                   



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
    num_guesses=6
    num_warnings=3
    letters_guessed=[]
    vowels=["a","e","i","o","u"]
    guessed = False
    sw_list=[]
    for char in secret_word:
        sw_list.append(char)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word with ",(len(secret_word))," letters long.")
    print("------------------")
    while num_guesses > 0:
        print("You have ",num_warnings," warnings left.")
        print("You have ",num_guesses," guesses left.")
        availabe_letters=get_available_letters(letters_guessed)
        print(availabe_letters)
        guess_letter=input("Please guess a letter: ")
        if guess_letter.isalpha():
            gl=guess_letter.lower()
            guess_letter=gl
            if guess_letter in letters_guessed:
                num_warnings = num_warnings-1
                if num_warnings <= 0:
                    num_guesses = num_guesses-1
                    num_warnings == 0
                print("Oops! You already guessed that letter.")
                print("-----------------")
            else:
                letters_guessed.append(guess_letter)
                current_guess=get_guessed_word(secret_word, letters_guessed)
                if guess_letter in sw_list:
                    print("Good guess: ",current_guess)
                    print("-------------------")
                    a=letters_guessed
                    guessed = is_word_guessed(secret_word, a)
                    if guessed == True:
                        break
                else:
                    print("Oops! That letter is not in my word: ",current_guess)
                    print("--------------------------")
                    if guess_letter in vowels:
                        num_guesses=num_guesses-2
                    else:
                        num_guesses=num_guesses-1      
        elif guess_letter == "*":
            mw = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(mw)
        else:
            num_warnings = num_warnings-1
            if num_warnings <= 0:
                num_guesses = num_guesses-1
                num_warnings == 0
            print("Oops! That is not a valid letter.")
    if guessed == True:
        print("Congratulations, you won!")
        char_score=0
        char_list= []
        for char in secret_word:
            if char not in char_list:
                char_score +=1
                char_list.append(char)
        score = char_score*num_guesses
        print("Your total score for this game is: ",score)
    else:
        print("Sorry, you ran out of guesses.")
        print("The word is",secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
hangman_with_hints("soft")

if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

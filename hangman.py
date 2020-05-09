def update_dashes_helper(secret, dashes, guess, i):
    """''
    Helper function that consumes a word, secret, and fills up the dashes with
    the guess if it is a part of the secret in the position of the word using
    the index i

    update_dashes_helper: Str Str Str Num => Str
    """
    if i >= len(secret):
        return dashes
    else:
        if secret[i: i + 1] == guess:
            return update_dashes_helper(secret, dashes[0:i] + guess + dashes
            [i + 1:len(dashes) + 1], guess, i + 1)
        else:
            return update_dashes_helper(secret, dashes, guess, i + 1)


def update_dashes(secret, dashes, guess):
    '''''
    update_dashes consumes the secret word, dashes and the guess just like in
    the hangman game.

    update_dashes: Str Str Str => Str
    Requires len(secret) = len(dashes)
    Requires len (guess) == 1
    Requires len (secret) > 0
    Requires len (dashes) > 0

    Examples:
    update_dashes("bubble", "------", "b") => "b-bb--"
    update_dashes("bubble", "b-bb--", "e") => "b-bb-e"
    update_dashes("python", "p-----", "x") => "p-----"
    '''
    return update_dashes_helper(secret, dashes, guess, 0)


secret_word = "Enter secret word:"
guess_letter = "Enter your guess:"
not_in_word = "Letter Not In Word"
invalid_input = "Invalid Input."
hangman_figures = [
'''         +---+
         |   |
             |
             |
             |
             |
      =========''',
'''        +---+
        |   |
        O   |
            |
            |
            |
      =========''',
'''        +---+
        |   |
        O   |
        |   |
            |
            |
      =========''',

'''        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========''',
'''        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========''',
'''        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========''',

'''       +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========''']


def hangman():
    s_w = str(input(secret_word))
    while (not s_w.isalpha()) or (len(s_w) < 1):
        return invalid_input

    dashes_word = (len(s_w)) * "_"



    i = 0
    new_list = []
    while i < len(hangman_figures):
        g_l = str(input(guess_letter))
        while (not g_l.isalpha()) or (len(g_l) != 1):
            print(invalid_input)
            return invalid_input
        if g_l in new_list:
            print("Already guessed!")

        elif g_l in s_w:
            new_list.append(g_l)
            i = i + 0
            dashes_word = update_dashes(s_w, dashes_word, g_l)
            print(update_dashes(s_w, dashes_word, g_l))
            print(hangman_figures[i])
            if dashes_word == s_w:
                print("You Won.")
                break
        elif g_l not in s_w:
            new_list.append(g_l)
            i = i + 1
            print(update_dashes(s_w, dashes_word, g_l))
            print(hangman_figures[i])
            if i == (len(hangman_figures) - 1):
                print("Game Over!")
                break
 
hangman()
                   
            

            
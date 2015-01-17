# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28


# This function will clean the 'message' by returning an uppercase version of
# the message
def clean_message(message):

    '''(str)-> str
    Return a string of the 'message' that only includes its alphabetical
    characters in uppercase form.

    >>> clean_message('bob')
    'BOB'
    >>> clean_message('s A Mm Y')
    'SAMMY'
    >>> clean_message('do$%gG!@Y')
    'DOGGY'
    
    '''
    empty_string = ''
    for ch in message:
        if ch.isalpha():
            empty_string += ch.upper()
    return empty_string

# This function will encrypt a character by applying a keystream value to it
def encrypt_letter(single_character, keystream_value):

    '''(str, int)-> str
    Return the encrypted charcter of 'single_charcter' after appying the
    'keystream_value' to it.

    >>> encrypt_letter('B', 12)
    'N'
    >>> encrypt_letter('A', 11)
    'L'
    
    '''
    a = ord(single_character)
    a += keystream_value
    if(a > 90):
        a = a - 26
    return chr(a)

# This function will decrypt a character by applying a keystream value to it
def decrypt_letter(single_character, keystream_value):

    '''(str, int)-> str
    Return the decrypted charcter of 'single_charcter' after appying the
    'keystream_value' to it.

    >>> decrypt_letter('N', 12)
    'B'
    >>> decrypt_letter('L', 11)
    'A'
    
    '''  
    a = ord(single_character)
    a = a - keystream_value
    if a < 65:
        a += 26
    return chr(a)

# This function will swap a card with an index indicated with the following card
# after that index 
def swap_cards(deck_of_cards, num_card):
    
    '''(list of int, int)-> NoneType 
    Swaps the card at index (num_card) with the following card for the
    deck_of_cards.

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6,
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> swamp_cards(deck_of_cards, 3)
    >>> deck_of_cards
    [1, 4, 7, 13, 10, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27,
    2, 5, 8, 11, 14, 17, 20, 23, 26]
    
    '''    
    picked_card = deck_of_cards[num_card]
    bottom_card = deck_of_cards[-1]
    if num_card == ((len(deck_of_cards) - 1) or -1):
        deck_of_cards[-1] = deck_of_cards[0]
        deck_of_cards[0] = bottom_card    
    else:
        deck_of_cards[num_card] = deck_of_cards[num_card + 1]
        deck_of_cards[num_card + 1] = picked_card


# Swap JOKER1 with the card following it 
def move_joker_1(deck_of_cards):
    
    '''(list of int)-> NoneType
    Find joker1 and swap it with the card following it.

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,
    6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_joker_1(deck_of_cards)
    >>> deck_of_cards
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    2, 27, 5, 8, 11, 14, 17, 20, 23, 26]

    ''' 
    swap_cards(deck_of_cards, deck_of_cards.index(JOKER1))

# Move JOKER2 down two cards (using swap function) 
def move_joker_2(deck_of_cards):

    '''(list of int)-> NoneType
    Find joker2 and move it two cards down.

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_joker_2(deck_of_cards)
    >>> deck_of_cards
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15, 18, 21, 24,
    2, 27, 5, 8, 11, 14, 17, 20, 23, 26]
    
    '''
    swap_cards(deck_of_cards, deck_of_cards.index(JOKER2))
    swap_cards(deck_of_cards, deck_of_cards.index(JOKER2))
        
# Performs step 3 of the algorithm by swaping cards above and below the
# two jokers 
def triple_cut(deck_of_cards):
    
    '''(list of int)-> NoneType
    Every card above the first joker goes after the second joker and
    every card after the second joker goes in front of the first joker.

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9,
    12, 15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(deck_of_cards)
    >>> deck_of_cards
    [5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4,
    7, 10, 13, 16, 19, 22, 25, 3, 6]

    '''
    index_joker_1 = deck_of_cards.index(JOKER1)
    index_joker_2 = deck_of_cards.index(JOKER2)
    if index_joker_1 < index_joker_2:
        above_joker_cards = deck_of_cards[0:index_joker_1]
        below_joker_cards = deck_of_cards[index_joker_2 + 1:]
        middle_cards = deck_of_cards[index_joker_1: index_joker_2 + 1]
        temp_list = below_joker_cards + middle_cards + above_joker_cards
        for i in range(len(deck_of_cards)):
            deck_of_cards[i] = temp_list[i] 
    elif index_joker_1 > index_joker_2:
        above_joker_cards = deck_of_cards[0:index_joker_2]
        below_joker_cards = deck_of_cards[index_joker_1 + 1:]
        middle_cards = deck_of_cards[index_joker_2: index_joker_1 + 1]
        temp_list = below_joker_cards + middle_cards + above_joker_cards
        for i in range(len(deck_of_cards)):
            deck_of_cards[i] = temp_list[i]

# This function takes the number cards indicated by the bottom card of the deck
# and then moves them to just above the bottom card 
def insert_top_to_bottom(deck_of_cards):

    '''(list of int)-> NoneType
    Move the number of cards(as per the bottom card) from the top of the
    deck to just above the bottom card.

    >>> deck_of_cards = [5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12, 15, 18,
    21, 24, 2, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6]
    >>> insert_top_to_bottom(deck_of_cards)
    >>> deck_of_cards
    [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16, 19,
    22, 25, 3, 5, 8, 11, 14, 17, 20, 6]

    '''
    empty_deck = []
    bottom_card = deck_of_cards[-1]
    if bottom_card != JOKER2:
        empty_deck += deck_of_cards[bottom_card:-1]
        empty_deck += deck_of_cards[0:bottom_card]
        empty_deck.append(bottom_card)
    elif bottom_card == JOKER2:
        bottom_card = JOKER1
        empty_deck += deck_of_cards[bottom_card:27]
        empty_deck += deck_of_cards[0:bottom_card]
        empty_deck.append(deck_of_cards[JOKER1])
    for card in range(len(deck_of_cards)):
        deck_of_cards[card] = empty_deck[card]

# This functions takes the value of the top card and treats it as an index
# and then returns that index as a keystream value 
def get_card_at_top_index(deck_of_cards):
    
    '''(list of int)-> int
    Look at the top card vaue and use it as an index, then return the
    card at that index from the 'deck_of_cards'(this is a keystream value).

    >>> deck_of_cards = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4,
    7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> get_card_at_top_index(deck_of_cards)
    11
    
    '''
    card_index = deck_of_cards[0]
    if card_index == JOKER2:
        return deck_of_cards[JOKER1]
    elif card_index != JOKER2:
        return deck_of_cards[card_index]

# This function does all five steps of the algorithm and returns the keystream
# value at the end 
def get_next_value(deck_of_cards):

    '''(list of int)-> int
    Return the next potential keystream value (after another round of
    the algorithm where the steps are repeated)

    >>> deck_of_cards = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4,
    7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> get_next_value(deck_of_cards)
    9
    
    '''
    move_joker_1(deck_of_cards)
    move_joker_2(deck_of_cards) 
    triple_cut(deck_of_cards)
    insert_top_to_bottom(deck_of_cards)
    return get_card_at_top_index(deck_of_cards)
        
    
# This function returns keystream values within the range of 1 to 26 
def get_next_keystream_value(deck_of_cards):

    '''(list of int)-> int
    Return a potential keystream value within the range of 1 to 26. 

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(deck_of_cards)
    11
    >>> get_next_keystream_value(deck_of_cards)
    9

    '''
    keystream_value = get_next_value(deck_of_cards)
    while not(1 <= keystream_value and keystream_value <= 26):
        keystream_value = get_next_value(deck_of_cards)
    return keystream_value

# This function processes (encrypts or decrypts) a single message 
def process_message(deck_of_cards, message, encrypt_decrypt):

    '''(list of int, str, str)-> str
    Return the encrypted or decrypted message from 'message'
    (as per the variable 'encrypt_decrypt') by using keystream values
    from 'deck_of_cards'.

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck_of_cards, 'Hello World', 'e')
    'SNISYVZCSL'
    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck_of_cards, 'SNISYVZCSL', 'd')
    'HELLOWORLD' 

    ''' 
    cleaned_message = clean_message(message)
    if encrypt_decrypt == 'e':
        encrypted_message = ""
        keystream_value_list = [] 
        for ch in cleaned_message:
            keystream_value_list.append(get_next_keystream_value(deck_of_cards))
        for i in range(len(cleaned_message)):
            encrypted_message += encrypt_letter(cleaned_message[i], keystream_value_list[i])
        return encrypted_message
    elif encrypt_decrypt == 'd':
        decrypted_message = ""
        keystream_value_list = [] 
        for ch in cleaned_message:
            keystream_value_list.append(get_next_keystream_value(deck_of_cards))
        for i in range(len(cleaned_message)):
            decrypted_message += decrypt_letter(cleaned_message[i], keystream_value_list[i])
        return decrypted_message
    
# This function processes (encrypts or decrypts) a list of messages 
def process_messages(deck_of_cards, messages, encrypt_decrypt):

    '''(list of int, list of str, str)-> list of str
    Return a list of encrypted or decrypted messages from 'messages'
    (as per the variable 'encrypt_decrypt') by using keystream values
    from 'deck_of_cards'.

    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,
    6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_messages(deck_of_cards, ['Hello World', 'Bob', 'hockey night'],
    'e')
    ['SNISYVZCSL', 'KZM', 'HMHTYPFRWAQ']
    >>> deck_of_cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_messages(deck_of_cards, ['SNISYVZCSL', 'KZM', 'HMHTYPFRWAQ'],
    'd')
    ['HELLOWORLD', 'BOB', 'HOCKEYNIGHT']

    '''
    empty_list_messages = []
    for message in messages:
        empty_list_messages.append(process_message(deck_of_cards, message, encrypt_decrypt))
    return empty_list_messages
        
# This function reads a 'message_file' opened in main() and returns it as a list
# of strings 
def read_messages(message_file):

    '''(file open for reading)-> list of str
    Read and return the contents of the 'message_file' as a list of strings 

    '''
    message = message_file.readlines() 
    for i in range(len(message)):
        message[i] = message[i].strip()
    return message

# This function reads a 'deck file' opened in main() and returns it as a list
# of integers 
def read_deck(deck_file):

    '''(file open for reading)-> list of int
    Read and return the contents of the 'deck_file' as a list of strings 

    '''
    cards = deck_file.readlines() 
    new_deck = []
    new_string_list = []
    for i in range(len(cards)):
        cards[i] = cards[i].strip()
    for strings in cards:
        new_string_list.append(strings.split())
    for lists in new_string_list:
        for string in lists:
            new_deck.append(int(string))
    return new_deck
            
            
        
            
    

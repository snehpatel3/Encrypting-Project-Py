"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message_file1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.

# Encryption or decryption performed here 
def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    message_file = open(MSG_FILENAME, 'r')
    deck_file = open(DECK_FILENAME, 'r')

    deck_of_cards = cipher_functions.read_deck(deck_file)
    messages = cipher_functions.read_messages(message_file)

    print(cipher_functions.process_messages(deck_of_cards, messages, MODE))
    
    pass

main()

# Transposition Cipher Decryption
# http://inventwithpython.com/codebreaker (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    translated = decryptMessage(myKey, myMessage)

    # Print the (decrypted) string in translated to the screen, with
    # a | (called "pipe" character) after it in case there are spaces at the
    # end of the decrypted message.
    print(translated + '|')

    # Copy the (decrypted) string in translated to the clipboard.
    pyperclip.copy(translated)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a Python
    # list of strings. First, we need to calculate a few values.

    # The number of "columns" our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # The number of "rows" our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the transposition grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next character
    # in the encrypted message will go.
    col = 0
    row = 0

    for i in range(len(message)):
        plaintext[col] += message[i]
        col += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()

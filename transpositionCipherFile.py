# Transposition Cipher Encrypt File
# http://inventwithpython.com/codebreaker (BSD Licensed)

import math, time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.encrypted.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists, this
    # program will overwrite that file.
    outputFilename = 'frankenstein.decrypted.txt'
    myKey = 42
    myMode = 'decrypt' # set to 'encrypt' or 'decrypt'

    # If the input file does not exist, then the program terminates early on.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption takes.
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    print('%sion time: %s seconds' % (myMode.title(), round(time.time() - startTime, 3)))

    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == '__main__':
    main()
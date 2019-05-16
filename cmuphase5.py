def cmuBombPhase5():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    andedAlphabet = []
    scrambledString = "isrveawhobpnutfg  "
    goalString = "giants"
    indicesInString = []
    string = ""
    andValue = 0xf

    #get the indices for the target string within the scrambled string
    for charIndex in range(len(goalString)):
        char = goalString[charIndex]
        indicesInString.append(scrambledString.index(char))

    #create a array holding each of the values after anding
    for charIndex in range(len(alphabet)):
        hexvalue = ord(alphabet[charIndex])
        andedAlphabet.append(hexvalue & andValue)

    #get the string that "decrypts" to goal string
    for i in range (len(indicesInString)):
        indexOfTargetString = indicesInString[i]
        #get index within actual alphabet
        indexInAlphabet = andedAlphabet.index(indexOfTargetString)
        string+= alphabet[indexInAlphabet]

    #prints the scrambled string
    print("scrambled:", string)

#version 2 that does a simple shift (avoids going through entire alphabet)
#unsure if this works for all cases
def cmuBombPhase5Ver2():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    scrambledString = "isrveawhobpnutfg  "
    goalString = "giants"
    indicesInString = []
    string = ""

    #get the indices for the target string within the scrambled string
    for charIndex in range(len(goalString)):
        char = goalString[charIndex]
        indicesInString.append(scrambledString.index(char))

    #get the string that "decrypts" to goal string
    for i in range (len(indicesInString)):
        indexOfTargetString = indicesInString[i]
        newIndex = (indexOfTargetString - 33) % 16 #16 because 16 possible values
        #get index within actual alphabet
        string+= alphabet[newIndex]

    #prints the scrambled string
    print("scrambled:", string)
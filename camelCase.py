def dislplay_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print ('\n', stars, '\n', msg, '\n', stars, '\n')

def display_instructions():
    msg = "Please enter a sentence or text to convert it to camelCase"
    lines = "_" * len(msg)
    print('\n', lines, '\n', msg, '\n', lines, '\n')

def lowercase(userString):
    newString = userString.lower()
    return newString

def camel_Case(newString):

    lowerString = newString.split(' ')
    #split the user input up by the spaces provided
    #while making all input lowercase
    numOfWords = lowerString.__len__()
    #figure out how many words there are
    count = 0
    #use count to keep the first word lowercase
    list1 = []

    while numOfWords > count:
        #do not exceed the number of words to keep list in range
        eachWord = lowerString[count]

        if count != 0:
            #add each word to the list and capitalize the first letter
            #increase the count
            list1.append(eachWord.title())
            count += 1

        elif count == 0:
                #add the first word to the list and keep it lowercase
            list1.append(eachWord)
            count += 1

    #finally, concatonate the string for display
    camelCaseString = ''.join(map(str, list1))
    return camelCaseString

def main():
    dislplay_banner()
    display_instructions()
    userString = input('')
    newString = lowercase(userString)
    finalCamelCase = camel_Case(newString)
    print(finalCamelCase)


if __name__ == '__main__':
    main()

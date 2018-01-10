print('Please enter a sentance or text to convert it to camelCase ')
string = input()
#get input from user
newString = string.lower().split(' ')
#split the user input up by the spaces provided
#while making all input lowercase
numOfWords = newString.__len__()
#figure out how many words there are
count = 0
#use count to keep the first word lowercase
list1 = []
while numOfWords > count:
#do not exceed the number of words to keep list in range
    eachWord = newString[count]
    if count != 0:
#add each word to the list and capitalize the first letter
#increase the count
        list1.append(eachWord.title())
        count += 1
    if count == 0:
#add the first word to the list and keep it lowercase
        list1.append(eachWord)
        count += 1
#finally, concatonate the string for display
camelCase = ''.join(map(str, list1))
print(camelCase)

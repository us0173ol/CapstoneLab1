print('Please enter text to convert it to camelCase')
string = input()

newString = string.lower().split(' ')
numOfWords = newString.__len__()
count = 0
list1 = []
while numOfWords > count:
    eachWord = newString[count]
    if count != 0:
        #print(eachWord.title())
        list1.append(eachWord.title())
        count += 1
    if count == 0:
        #print(eachWord)
        list1.append(eachWord)
        count += 1

#print(numOfWords)
#print(list1)
camelCase = ''.join(map(str, list1))
print(camelCase)

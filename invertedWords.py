#Create a function that received a char text
#this function should reorder the text backward
#If we give the word "Hola mundo" it should returns "odnum aloH"

finalText = ''
word = input('Type the text to reorder')

for vChar in word:
    arrayText.append(vChar)

arrayText.reverse()

for value in arrayText:
    finalText += value

print('The original text was: ' + word)
print('The reorder text is:  ' + finalText)

string = input('Enter the string:')

words = set()

result = ''

for word in string.split():
    if word not in words:
        result = result + word + ' '
        words.add(word)

print("After removing Duplicate values the strinig is : "+result)

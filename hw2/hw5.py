word = input("a 들어간 단어 : ")
index = word.find('a')
print(word[:index + 1])
print(word[index + 1:])
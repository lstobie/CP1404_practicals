text = input("text: ")
words_used = {}
new_word = ''
for word in text:
    if word == ' ':
        words_used[new_word] = 1
    elif new_word in text:
        words_used[new_word] += 1
    new_word += word
for word in words_used:
    print("{} {}".format(word, words_used[word]))



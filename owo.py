
dictionary = {'you': 'yuw', 'and': 'awnd', 'lol': 'lawl'}


def owo(text):
    words = text.split()
    for i in range(0, len(words)):
        word = words[i]
        if word in dictionary:
            words[i] = dictionary[word]
            text = ' '.join(words)

    text = text.replace('l', 'w')
    text = text.replace('r', 'w')

    return text

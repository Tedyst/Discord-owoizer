import unicodedata


def is_lower(s):
    return all(ord(c) < 123 and ord(c) > 96 for c in s)


def is_upper(s):
    return all(ord(c) < 91 and ord(c) > 63 for c in s)


def converted(message):
    translated = ""
    for letter in message:
        if letter == "B" or letter == "b":
            translated += unicodedata.lookup(
                'NEGATIVE SQUARED LATIN CAPITAL LETTER B')
        elif is_lower(letter):
            translated += unicodedata.lookup('REGIONAL INDICATOR SYMBOL LETTER ' +
                                             letter)
        elif is_upper(letter):
            translated += unicodedata.lookup('REGIONAL INDICATOR SYMBOL LETTER ' +
                                             letter)
        else:
            translated += letter
        translated += " "
    return translated

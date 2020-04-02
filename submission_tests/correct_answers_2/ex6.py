def get_acronym(phrase, connector='.'):
    return connector.join(i[0] for i in phrase.split() if i[0].isupper())


if __name__ == '__main__':
    print(get_acronym('Federal Bureau of Investigation'))
    print(get_acronym('Customs and Border Protection', ' '))
    print(get_acronym('Central Intelligence Agency', ''))

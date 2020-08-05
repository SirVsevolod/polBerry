def search4vowels(word: str) ->set:
    """Выводит главсные, найденные во введенном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(word: str, letters: str = 'aeiou') ->set:
    """Выводит найденные веденые буквы в веденном слове"""
    return set(letters).intersection(set(word))

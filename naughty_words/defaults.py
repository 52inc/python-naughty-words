import pkgutil
from naughty_words import NaughtyWords
from naughty_words.preprocessors import EmptyPreprocessor
from naughty_words.filters import CommonSubstitutions

data = pkgutil.get_data(__name__, 'wordlists/profanities.txt')
profanity_list = data.decode('utf-8').split('\n')


def has_profanity(text, additional=None, blacklist=None, profanities=None):
    if not profanities:
        global profanity_list
        profanities = profanity_list
    if additional:
        profanities = list(set(profanities).update(set(additional)))
    if blacklist:
        profanities = list(set(profanities).difference(set(blacklist)))
    naughty_words = NaughtyWords(preprocessors=[EmptyPreprocessor()],
                                 filters=[CommonSubstitutions()],
                                 profanities=profanities)
    return len(naughty_words.run_filters(text, only_first=True)) != 0


def get_all_profanity(text, additional=None, blacklist=None, profanities=None):
    if not profanities:
        global profanity_list
        profanities = profanity_list
    if additional:
        profanities = list(set(profanities).update(set(additional)))
    if blacklist:
        profanities = list(set(profanities).difference(set(blacklist)))
    naughty_words = NaughtyWords(preprocessors=[EmptyPreprocessor()],
                                 filters=[CommonSubstitutions()],
                                 profanities=profanities)
    return naughty_words.run_filters(text, only_first=False)

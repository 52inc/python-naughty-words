import re
import collections
from naughty_words.profanity.profanities import naughty_word_list
from difflib import SequenceMatcher


class NaughtyWords(object):

    def __init__(self, filters, text, delimiter=","):
        assert isinstance(filters, collections.Iterable) or isinstance(filters, str), \
            "Filters and objects to filter must be iterable or string."
        assert isinstance(text, str) or text is None, 'Text to filter must be a string'
        self.text = text
        if isinstance(filters, str):
            self.naughty_words = filters.split(delimiter)
        else:
            self.naughty_words = filters

    def _preprocess(self):
        pass

    def _algorithm(self, match_type='first'):
        if self.naughty_words is None or self.text is None:
            return None
        if match_type is not 'first':
            words = []

        for word in self.naughty_words:
            if self.dumb_string_match(word):
                if match_type is not 'first':
                    words.append(word)
                else:
                    return word
            elif self.regex_string_match(word):
                if match_type is not 'first':
                    words.append(word)
                else:
                    return word

        if match_type is not 'first':
            return words if words is not [] else None
        else:
            return None

    def dumb_string_match(self, word):
        return word in self.text

    def regex_string_match(self, word):
        alpha_num_word = re.sub('\W', '', word)
        pattern = self.profanity_expression(alpha_num_word)
        return re.search(pattern, self.text)

    @classmethod
    def escaped_expression(self, characters, escaped_characters, quantifier='*?'):
        re_expressions = escaped_characters
        for character in characters:
            re_expressions.append(re.escape(character))
        return f"[{''.join(re_expressions)}]{quantifier}"

    def profanity_expression(self, word):
        separating_expression = self.escaped_expression('a-zA-Z', ['^'])
        return r''.join(self.escaped_expression(character, [], '+?') + separating_expression for character in word)

    def first_match(self):
        self._preprocess()
        return self._algorithm()

    def all_matches(self):
        self._preprocess()
        return self._algorithm(match_type='all')

    def has_profanity(self):
        self._preprocess()
        return self._algorithm() is not None

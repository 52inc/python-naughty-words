import re
import collections

from typing import Optional, Iterable, Tuple, Type, Sequence


class ProfanityException(Exception):
    pass


class Preprocessor(object):
    """
    Abstract preprocessor for text
    """

    def process(self, text: str, context: dict) -> Tuple[str, dict]:
        """
        Preprocess text (substitutions, duplicates, etc.)

        :param text: text to be processed
        :param context: additional context to be passed to processors in the chain
        :return: tuple containing the processed text and updated context object
        """

        raise NotImplementedError()


class Filter(object):
    """
    Abstract filter for naughty words
    """

    def filter(self, text: str,
               context: dict,
               only_first: bool=True,
               raise_on_match: bool= False) -> Optional[Sequence[str]]:
        """
        Filter text, returning a list of profanity discovered

        :param text: text to process
        :param context: context dictionary from preprocessors or other filters
        :param only_first: whether to stop matching on the first detected profanity
        :param raise_on_match: whether to raise a ProfanityException on detection of profanity
        :return: list of profane words discovered
        """

        raise NotImplementedError()


class NaughtyWords(object):
    def __init__(self,
                 preprocessors: Iterable[Type[Preprocessor]]=None,
                 filters: Iterable[Type[Filter]]=None):

        self._preprocessors = []
        self._filters = []
        self._context = {}

        for p in preprocessors:
            assert isinstance(p, Preprocessor), "Attempted to register an invalid preprocessor"
            self._preprocessors.append(p)

        for f in filters:
            assert isinstance(f, Filter), "Attempted to register an invalid filter"
            self._filters.append(p)

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

    def run_filters(self, text, **kwargs):
        cur_text = text
        cur_context = {}

        for pre in self._preprocessors:
            cur_text, cur_context = pre(cur_text, cur_context)

        # TODO: Loop through, run all filters
        pass

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

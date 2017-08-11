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
                 filters: Iterable[Type[Filter]]=None,
                 profanities: Sequence[str] = None):

        self._preprocessors = []
        self._filters = []
        self._context = {'profanities': profanities}

        for p in preprocessors:
            assert isinstance(p, Preprocessor), "Attempted to register an invalid preprocessor"
            self._preprocessors.append(p)

        for f in filters:
            assert isinstance(f, Filter), "Attempted to register an invalid filter"
            self._filters.append(f)

    def run_filters(self, text, **kwargs):
        cur_text = text
        cur_context = self._context

        for pre in self._preprocessors:
            cur_text, cur_context = pre.process(cur_text, cur_context)

        # TODO: Loop through, run all filters
        matches = []
        for filter in self._filters:
            if kwargs['only_first']:
                match = filter.filter(cur_text, cur_context, **kwargs)
                if match is not []:
                    return match
            else:
                matches.extend(filter.filter(cur_text, cur_context, **kwargs))
        return matches if matches is not [] else None
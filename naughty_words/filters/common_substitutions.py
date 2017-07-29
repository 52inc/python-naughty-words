import re
from naughty_words.filters.base import NaughtyWords
from naughty_words.utils.confusables import standard_character_substitutions, separating_characters


class CommonSubstitutions(NaughtyWords):

    def profanity_expression(self, word):
        expression = ''
        separating_expression = self.escaped_expression(separating_characters, ['\s'])
        for character in word:
            expression = expression + self.escaped_expression(standard_character_substitutions[character], [], '+?') + separating_expression
        return expression

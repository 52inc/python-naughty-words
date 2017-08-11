import re
from naughty_words import Filter, ProfanityException
from naughty_words.utils.confusables import standard_character_substitutions, separating_characters


class CommonSubstitutions(Filter):

    @classmethod
    def escaped_expression(cls, characters, escaped_characters, quantifier='*?'):
        re_expressions = escaped_characters
        for character in characters:
            re_expressions.append(re.escape(character))
        return f"[{''.join(re_expressions)}]{quantifier}"

    def profanity_expression(self, word):
        expression = ''
        separating_expression = self.escaped_expression(separating_characters, ['\s'])
        for character in word:
            try:
                expression = expression + self.escaped_expression(standard_character_substitutions[character], [], '+?') + separating_expression
            except KeyError:
                expression = expression + self.escaped_expression(character, [], '+?') + separating_expression

        return expression

    def filter(self, text: str,
               context: dict,
               only_first: bool=True,
               raise_on_match: bool= False):
        profanities = context['profanities']
        matches = []
        for profanity in profanities:
            # TODO add solidified case for stopping emoji
            alpha_num_word = re.sub('\W', '', profanity)
            if alpha_num_word is '':
                continue
            pattern = self.profanity_expression(alpha_num_word)
            if re.search(pattern, text):
                if raise_on_match:
                    raise ProfanityException()
                elif only_first:
                    matches.append(profanity)
                    return matches
                else:
                    matches.append(profanity)
        return matches



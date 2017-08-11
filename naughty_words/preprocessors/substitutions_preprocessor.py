import re
from naughty_words import Preprocessor
from naughty_words.utils.confusables import standard_character_substitutions


class SubstitutionsPreprocessor(Preprocessor):

    def split(self, list):
        return list[:len(list)//2], list[len(list)//2:]

    def find_valid_subs(self, text, list_of_characters):
        if re.search(r'{}'.format(list_of_characters), text):
            if len(list_of_characters) > 1:
                list_a, list_b = self.split(list_of_characters)
                sub_list_a = self.find_valid_subs(text, list_a)
                sub_list_b = self.find_valid_subs(text, list_b)

                return sub_list_a + sub_list_b
            else:
                return list_of_characters
        else:
            return []

    def process(self, text: str, context: dict):
        try:
            cur_substitutions = context['character_substitutions']
        except KeyError:
            cur_substitutions = standard_character_substitutions

        final_subs = cur_substitutions.copy()
        for key, value in cur_substitutions.items():
            valid_subs = self.find_valid_subs(text, value)
            if len(valid_subs) == 0:
                final_subs.pop(key, None)
            else:
                final_subs[key] = valid_subs

        context['character_substitutions'] = final_subs
        return text, context
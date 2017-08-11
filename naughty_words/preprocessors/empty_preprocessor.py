from naughty_words import Preprocessor


class EmptyPreprocessor(Preprocessor):
    def process(self, text: str, context: dict):
        return text, context

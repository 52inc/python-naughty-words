import pytest
import time

from naughty_words.defaults import has_profanity

def test_default_filter_no_match():
    assert has_profanity("No profanity here") is False
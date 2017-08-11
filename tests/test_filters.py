import pytest
import time

from naughty_words.defaults import has_profanity


def test_default_filter_no_match():
    assert has_profanity("No ducking profanity here") is False


def test_default_filter_has_match():
    assert has_profanity("You fucking know there's profanity here") is True


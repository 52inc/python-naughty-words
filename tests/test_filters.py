import pytest
import time

from naughty_words.filters import NaughtyWords
from naughty_words.filters import CommonSubstitutions


def test_default_filter_no_match():
    nw_filter = NaughtyWords(['fuck'], 'There are no ducking words here.')
    assert nw_filter.has_profanity() is False
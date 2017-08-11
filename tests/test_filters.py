import pytest
import time

from naughty_words.defaults import has_profanity, get_all_profanity


def test_default_filter_no_match():
    assert has_profanity("No ducking profanity here") is False


def test_default_filter_has_match():
    assert has_profanity("You fucking know there's profanity here") is True


def test_get_all_profanity():
    assert get_all_profanity("My money's in that office, right? If she start giving me some bullshit about it ain't there, and we got to go someplace else and get it, I'm gonna shoot you in the head then and there. Then I'm gonna shoot that bitch in the kneecaps, find out where my goddamn money is. She gonna tell me too. Hey, look at me when I'm talking to you, motherfucker. You listen: we go in there, and that nigga Winston or anybody else is in there, you the first motherfucker to get shot. You understand?") == {'motherfuck', 'motherfucker', 'bullshit', 'bitchin', 'tit', 'shit', 'bitch', 'goddamn', 'damn', 'fucker', 'nigga',
     'fuck', 'mother fucker', 'god damn', 'mother-fucker'}
from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def text_mixedcase():
    assert shorten("Hello") == "HLL"

def test_novowel():
    assert shorten("lbcm") == "lbcm"
def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_empty_string():
    assert shorten("") == ""

def test_special_chars():
    assert shorten("h3ll0!") == "h3ll0!"


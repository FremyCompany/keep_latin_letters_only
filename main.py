import unicode_script_data
import unicodedata

import re

# import the lru_cache decorator from functools
from functools import lru_cache


emoji_punctuation = [
    # VARIATION SELECTORS
    u"\uFE00", u"\uFE01", u"\uFE02", u"\uFE03", u"\uFE04", u"\uFE05", u"\uFE06", u"\uFE07", u"\uFE08", u"\uFE09", u"\uFE0A", u"\uFE0B", u"\uFE0C", u"\uFE0D", u"\uFE0E", u"\uFE0F", 
    # ZERO WIDTH JOINER (ZWJ)
    u"\u200D",
]

@lru_cache(maxsize=1024)
def is_latin_or_numeric_or_punctuation(character):
    script, cat = unicode_script_data.script_cat(character)
    return script == 'Common' or script == 'Latin' or cat[0] in 'NSPZC' or character in emoji_punctuation

text = """
Here is a text with some non-Latin characters: 你好, мир, नमस्ते, العالم
Here is some text with only Latin characters (including accented versions of Latin characters): abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ àâäéèêëîïôöùûüÿ
Here are voyels with tilde which do not pass the regular expression: ãẽĩõũỹ
Here are some emojis, too: 😀🙃😉😍🤔🤷🏻‍♀️👩🏻‍💻
Here are some complex emojis which use ZWJ (like family emojis or skin tones): 👩🏻‍👩🏾‍👦🏿👨🏻‍👩🏻‍👧🏼👩🏻‍👩🏻‍👧🏼👨🏼‍👩🏼‍👧🏽‍👦🏿
"""

def remove_non_latin(text):
    # normalize the text to NFKC form, which will reunite any decomposed characters into their precomposed form
    text = unicodedata.normalize('NFKC', text)

    # this regular expression will match any character that is not Latin, numeric, or punctuation
    non_latin_regex = re.compile(r'[^-a-zàâäéèêëîïôöùûüÿ0-9,;.:!?<>\(\)\[\]\{\}\s]', re.UNICODE | re.IGNORECASE)

    # replace every non-Latin character with the output of the "replace_char_if_non_latin" function
    return non_latin_regex.sub(replace_char_if_non_latin, text)

def replace_char_if_non_latin(match):
    # match.group(0) will return the matched character
    match_char = match.group(0)

    # if the character is Latin or numeric or punctuation, return it as-is
    # otherwise, return an the replacement character of unicode U+FFFD (REPLACEMENT CHARACTER)

    # # debug code:
    # if is_latin_or_numeric_or_punctuation(match.group(0)):
    #     print("ALLOWING: " + match.group(0) + " " + str(ord(match.group(0))))
    # else:
    #     print("CENSURING: " + match.group(0) + " " + str(ord(match.group(0))))

    return match_char if is_latin_or_numeric_or_punctuation(match_char) else '\uFFFD'

print(text)
print(remove_non_latin(text))

#print('')
#print(unicode_script_data._compile_scripts_txt())
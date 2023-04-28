# keep_latin_letters_only
A python script to remove letters from non-latin script from a text, while keeping emojis and rare accented letters with diacritics

```py
text = """
Here is a text with some non-Latin characters: 你好, мир, नमस्ते, العالم
Here is some text with only Latin characters (including accented versions of Latin characters): abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ àâäéèêëîïôöùûüÿ
Here are voyels with tilde which do not pass the regular expression: ãẽĩõũỹ
Here are some emojis, too: 😀🙃😉😍🤔🤷🏻‍♀️👩🏻‍💻
Here are some complex emojis which use ZWJ (like family emojis or skin tones): 👩🏻‍👩🏾‍👦🏿👨🏻‍👩🏻‍👧🏼👩🏻‍👩🏻‍👧🏼👨🏼‍👩🏼‍👧🏽‍👦🏿
"""

print(remove_non_latin_chars(text))

"""
Here is a text with some non-Latin characters: ��, ���, ����, ������
Here is some text with only Latin characters (including accented versions of Latin characters): abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ àâäéèêëîïôöùûüÿ
Here are voyels with tilde which do not pass the regular expression: ãẽĩõũỹ
Here are some emojis, too: 😀🙃😉😍🤔🤷🏻‍♀️👩🏻‍💻
Here are some complex emojis which use ZWJ (like family emojis or skin tones): 👩🏻‍👩🏾‍👦🏿👨🏻‍👩🏻‍👧🏼👩🏻‍👩🏻‍👧🏼👨🏼‍👩🏼‍👧🏽‍👦🏿
"""
```

It is possible to modify the script to include or exclude more characters, the current filter is rather permissive.

I would recommend to optimize the code for the type of text you process. Add to the `non_latin_regex` regular expression all the frequently used characters in your dataset. The default set is acceptable, but may not include all the forms of punctuation which your text might use, triggering the replacement code more often than necessary (this is just a performance issue if you have a large dataset to process).

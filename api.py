from __future__ import unicode_literals


def convert_text(text):
    out = ''

    for word in text.split():
        out += 'ng{} '.format(word.capitalize())

    return out

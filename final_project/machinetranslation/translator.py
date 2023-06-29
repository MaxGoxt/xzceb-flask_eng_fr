# -*- coding: utf-8 -*-
""" Module translator """
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ Traductor de inglés a francés """
    if english_text is not None:
        french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
        return french_text
    return None


def french_to_english(french_text):
    """ Traductor de francés a inglés """
    if french_text is not None:
        english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
        return english_text
    return None

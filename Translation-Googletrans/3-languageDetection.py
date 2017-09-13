#!/usr/bin/python
# -*- coding: utf-8 -*-
import supportedLang

from googletrans import Translator
translator = Translator()
lst = translator.detect('이 문장은 한글로 쓰여졌습니다.')
language = lst.lang
print language
print supportedLang.supported_languages[language]
